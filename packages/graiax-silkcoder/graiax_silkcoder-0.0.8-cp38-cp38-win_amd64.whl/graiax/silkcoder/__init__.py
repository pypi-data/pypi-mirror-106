import os
import sys
import wave
import shlex
import asyncio
import audioop
import tempfile
import mimetypes
from io import BytesIO
from typing import Union
from pathlib import Path
from collections import namedtuple

from . import _silkv3
from .utils import (
	fsdecode, iswave, issilk, 
	makesureinput, makesureoutput,
	get_encoder_name)

class CoderError(Exception):
	"""所有编码/解码的错误"""
	pass

class SilkCoder:

	def __init__(self, pcm_data=None):
		"""注:pcm格式为24kHz 16bit mono"""
		self.pcm = tempfile.NamedTemporaryFile(mode="w+b", delete=False, suffix='.pcm')
		if pcm_data: self.pcm.write(pcm_data)

	def __del__(self):
		self.pcm.close()
		os.unlink(self.pcm.name)

	@classmethod
	@makesureinput(BytesIO_allowed=True)
	async def from_wav(cls, file, ss=0, t=0):
		"""
		从wav导入音频数据
		注:本函数只允许1-48000kHz 8-16bit wav
		如许转码不支持的wav，请使用from_file
		file是文件本身，也可以是BytesIO实例
		"""
		with wave.open(file, 'rb') as wav:
			wav_rate = wav.getframerate()
			wav_width = wav.getsampwidth()
			wav_channel = wav.getnchannels()
			if t:
				wav_data = wav.readframes((ss+t)*wav_width*wav_rate)[ss*wav_width*wav_rate:]
			else:
				wav_data = wav.readframes(wav.getnframes())
			converted = audioop.ratecv(wav_data, wav.getsampwidth(), wav_channel, wav_rate, 24000, None)[0]
			if wav_channel != 1: converted = audioop.tomono(converted, wav_channel, 0.5, 0.5)
			return cls(converted)

	@classmethod
	@makesureinput(BytesIO_allowed=False)
	async def from_file_though_tempfile(cls, file, audio_format, ss, t):
		"""
		通过ffmpeg/anconv从其他音频格式导入音频数据
		file可以是路径/二进制数据/BytesIO实例
		实现方法为通过tempfile
		"""
		c = cls()
		cmd = [get_encoder_name()]
		if audio_format is not None: cmd.extend(['-f', audio_format])
		cmd.extend(['-ss', ss, '-i', file, '-t', str(t)] if t else ['-i', file])
		cmd.extend(['-af', 'aresample=resampler=soxr', '-ar', '24000', '-ac', '1', '-y' ,
			'-loglevel', 'error', '-f', 's16le', c.pcm.name])
		shell = await asyncio.create_subprocess_exec(*cmd,
			stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		p_out, p_err = await shell.communicate()
		if shell.returncode != 0:
			raise CoderError(f"ffmpeg error:\n{p_err.decode(errors='ignore')}")
		return c

	@classmethod
	async def from_file(cls, file, audio_format, codec, ffmpeg_para, ss, t):
		"""
		通过ffmpeg/anconv从其他音频格式导入音频数据
		file可以是路径/二进制数据/BytesIO实例
		"""
		try:
			filename = fsdecode(file)
		except TypeError:
			filename = None

		c = cls()
		converter = get_encoder_name()
		cmd = [converter]
		if audio_format is not None: cmd += ['-f', audio_format]
		if codec: cmd += ["-acodec", codec]
		if filename:
			input_cmd = ['-i', filename]
			stdin_data = None
		else:
			if converter == 'ffmpeg':
				input_cmd = ["-read_ahead_limit", "-1", "-i", "cache:pipe:0"]
			else:
				input_cmd = ["-i", "-"]
			stdin_data = file.read() if isinstance(file, BytesIO) else file

		cmd += ['-ss', ss, *input_cmd, '-t', t] if t else input_cmd
		if ffmpeg_para: cmd += ffmpeg_para
		cmd += ['-af', 'aresample=resampler=soxr', '-ar', '24000', '-ac', '1',
			'-y' , '-vn', '-loglevel', 'error', '-f', 's16le', c.pcm.name]
		shell = await asyncio.create_subprocess_exec(*cmd,
			stdin=None if filename else asyncio.subprocess.PIPE,
			stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		p_out, p_err = await shell.communicate(input=stdin_data)
		if shell.returncode != 0:
			raise CoderError(f"ffmpeg error:\n{p_err.decode(errors='ignore')}")
		return c

	@classmethod
	@makesureinput(BytesIO_allowed=False)
	async def from_silk(cls, file):
		"""
		通过slk(silkv3)格式导入音频数据
		file可以是路径/二进制数据/BytesIO实例
		"""
		if not issilk(file):
			raise CoderError("File is not silkv3 format")
		c = cls()
		await asyncio.get_running_loop().run_in_executor(
			None, _silkv3.decode, file, c.pcm.name)
		return c

	@makesureoutput(BytesIO_allowed=True)
	async def to_wav(self, file=None):
		"""
		导出为24000Hz 16bit mono的wave
		file可以是路径/BytesIO实例
		如果file为None则返回二进制数据
		"""
		with wave.open(file, 'wb') as wav_out:
			self.pcm.seek(0)
			wav_out.setnchannels(1)
			wav_out.setframerate(24000)
			wav_out.setsampwidth(2)
			wav_out.writeframes(self.pcm.read())

	@makesureoutput(BytesIO_allowed=False)
	async def to_file(self, file=None, audio_format=None, codec=None, ffmpeg_para=None, metadata=None, rate=None):
		"""
		通过ffmpeg/anconv导出为其它格式的音频数据
		file可以是路径/BytesIO实例
		如果file为None则返回二进制数据
		"""
		# mp3文件在写入id3的时候要求output为seelable
		# 所以如果使用PIPE将会失败
		cmd = [get_encoder_name(), '-f', 's16le', '-ar', '24000', '-ac', '1', '-i', self.pcm.name]
		if audio_format is not None: cmd += ['-f', audio_format]
		if codec: cmd += ["-acodec", codec]
		if rate is not None: cmd += ['-ab', rate]
		if ffmpeg_para is not None: cmd += [str(a) for a in ffmpeg_para]

		if metadata is not None:
			for key, value in tags.items():
				cmd += ['-metadata', f'{key}={value}']

		if sys.platform == 'darwin' and codec == 'mp3':
			cmd += ["-write_xing", "0"]

		cmd.extend(['-y' ,'-loglevel', 'error', file])
		shell = await asyncio.create_subprocess_exec(*cmd)
		await shell.communicate()
		if shell.returncode != 0:
			raise CoderError(
				"Encoding failed. ffmpeg returned error code: {0}\n\nOutput from ffmpeg/avlib:\n\n{1}".format(
					p.returncode, p_err.decode(errors='ignore')))
		if file is None:
			return Path(file).read_bytes()

	@makesureoutput(BytesIO_allowed=False)
	async def to_silk(self, file=None, rate=65000):
		"""
		导出slk(silkv3)格式音频文件
		file可以是路径/BytesIO实例
		如果file为None则返回二进制数据
		"""
		await asyncio.get_running_loop().run_in_executor(
			None, _silkv3.encode, self.pcm.name, file, rate)

async def encode(
	input_voice: Union[os.PathLike, str, BytesIO, bytes], 
	output_voice: Union[os.PathLike, str, BytesIO, None]=None,
	audio_format: str=None, codec: str=None,
	ensure_ffmpeg: bool=False, rate: int=65000, 
	ffmpeg_para: list=None, ss: int=0, t: int=0
	) -> Union[bool, tuple]:
	"""
	将音频文件转化为silk文件

	Args:
		input_voice(os.PathLike, str, BytesIO, bytes) 输入文件
		output_voice(os.PathLike, str, BytesIO, None) 输出文件(silk)，默认为None
		audio_format(str) 音频格式(如mp3, ogg) 默认为None(此时将由ffmpeg/avconv解析格式)
		codec(str) 编码器(如果需要) 默认为None
		ensure_ffmpeg(bool) 在音频能用wave库解析时是否强制使用ffmpeg/anconv导入 默认为False
		rate(int) silk码率 默认为65000 区间为 (0,100000]
		ffmpeg_para(list) ffmpeg/avconc自定义参数 默认为None
		ss(int) 开始读取时间,对应ffmpeg/avconc中的ss(只能精确到秒) 默认为0(如t为0则忽略)
		t(int) 持续读取时间,对应ffmpeg/avconc中的t(只能精确到秒) 默认为0(不剪切)
		"""
	if not ensure_ffmpeg and iswave(input_voice):
		pcm = await SilkCoder.from_wav(input_voice, ss, t)
	else:
		pcm = await SilkCoder.from_file(input_voice, audio_format, codec, ffmpeg_para, ss, t)
	return await pcm.to_silk(output_voice)

async def decode(
	input_voice: Union[os.PathLike, str, BytesIO, bytes],
	output_voice: Union[os.PathLike, str, BytesIO, None]=None,
	audio_format: str=None, codec: str=None, 
	ensure_ffmpeg: bool=False, rate: int=None, 
	metadata:dict=None, ffmpeg_para: list=None) -> Union[bool, tuple]:
	"""
	将silkv3音频转换为其他音频格式

	Args:
		input_voice(os.PathLike, str, BytesIO, bytes) 输入文件(silk)
		output_voice(os.PathLike, str, BytesIO, None) 输出文件，默认为None
		audio_format(str) 音频格式(如mp3, ogg) 默认为None(此时将由ffmpeg/avconv解析格式)
		codec(str) 编码器(如果需要) 默认为None
		ensure_ffmpeg(bool) 在音频能用wave库解析时是否强制使用ffmpeg/anconv导入 默认为False
		rate(int) 码率 对应ffmpeg/avconc中"-ab"参数 默认为None
		metadata(dict) 音频标签 将会转化为ffmpeg/avconc参数 如"-metadata title=xxx" 默认为None
		ffmpeg_para(list) ffmpeg/avconc自定义参数 默认为None
	"""
	pcm = await SilkCoder.from_silk(input_voice)
	if isinstance(output_voice, (os.PathLike, str)):
		audio_format = fsdecode(output_voice).split('.')[-1]
	if ffmpeg_para is None and rate is None and metadata is None and audio_format in ['wav', None]:
		return await pcm.to_wav(output_voice)
	else:
		return await pcm.to_file(output_voice, audio_format, codec, ffmpeg_para, metadata, rate)