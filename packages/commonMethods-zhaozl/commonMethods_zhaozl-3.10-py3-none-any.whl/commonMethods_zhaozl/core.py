"""
Functions
----------
* code2Name: 通过输入词典对传入code进行转译同时使用_verbose控制是否显示对字典的预检验
* printWithColor: 打印具有颜色和特定格式的字符串
* mapminmax: 数据进行标准化[0，1]
* moduleOfDataframe: 计算一个dataframe所表达的多个向量的模
* cosineThetaOfVectors: 计算向量1（或多个向量1）与向量2的夹角余弦
* randomGrouping: 根据比例随机取得一数据表中的样本

Example
----------
>>> from commonMethods_zhaozl import code2Name, printWithColor

"""

import numpy as np  # numpy==1.18.5
import pandas as pd  # pandas==1.1.0


pd.set_option('display.max_columns', 10000, 'display.width', 10000, 'max_rows', 50,
              'display.unicode.east_asian_width', True)


def code2Name(_kksCodes: list, _dictNames: list, _kksCode: list, _verbose=True):
	"""
	通过输入词典对传入code进行转译同时使用_verbose控制是否显示对字典的预检验

	[1] 参数
	----------
	_kksCodes:
	    list, 编码的字典
	_dictNames:
	    list, 名称的字典
	_kksCode:
	    list, 需要转译的编码
	_verbose:
	    Boolean, 是否显示对输入字典和待转译编码的检查结果

	[2] 返回
	-------
	-/-:
	    list, 转译完成的名称

	[3] 示例1
	--------
	>>> a = code2Name(kksCode, dictName, ['ED009HP2MUB01UU008AA01J3DG006EA01'])
	>>> print(a)
	"""
	# 检查输入的清单是否符合基本要求
	len_kksCodes = len(_kksCodes)
	len_kksCodes_unique = len(pd.unique(_kksCodes))
	len_dictNames = len(_dictNames)
	len_dictNames_unique = len(pd.unique(_dictNames))
	if _verbose:
		checkStr01 = "待检编码中有重复项 X " if isinstance(_kksCode, list) and len(np.unique(_kksCode)) != len(
			_kksCode) else "待检编码中没有重复项 √ "
		checkStr02 = "编码中没有重复项 √ " if len_kksCodes == len_kksCodes_unique else "编码中有重复项 X "
		checkStr03 = "名称中没有重复项 √ " if len_dictNames == len_dictNames_unique else "名称中有重复项 (允许) "
		print("#" * 2 * (2 + max([len(checkStr01), len(checkStr02), len(checkStr03)])))
		print('\t', checkStr01, '\n\t', checkStr02, '\n\t', checkStr03)
		print("#" * 2 * (2 + max([len(checkStr01), len(checkStr02), len(checkStr03)])))
	# 字典以中文名称为依据，升序排列
	_dict = pd.DataFrame({'kksCodes': _kksCodes, 'dictNames': _dictNames}).sort_values(by=['dictNames'])
	# 查询
	_kksName = []
	if isinstance(_kksCode, list):
		for eachCode_toReplace in _kksCode:
			queryRes = _dict.query("kksCodes.str.contains(\'" + eachCode_toReplace + "\')", engine='python')
			res = queryRes['dictNames'].values
			if np.shape(res)[0] == 0:
				print(">>> 注意：对象kksCode未找到kksName，此kksCode是 %s" % (eachCode_toReplace))
			elif np.shape(res)[0] >= 2:
				print(">>> 错误: 单个kksCode对应了多个kksName，这些kksCode是%s，这些kksName是%s" % (
					queryRes['kksCodes'].values, queryRes['dictNames'].values))
			if res:
				_kksName = _kksName + res.tolist()
			else:
				_kksName.append(eachCode_toReplace)
		return _kksName


def printWithColor(_msg, _prefix="\n\n", _suffix="\n",
                   _displayStyle="default",
                   _fontColor="white",
                   _backColor=None):
	"""
	打印具有颜色和特定格式的字符串

	:param _msg: str, 需要打印的信息
	:param _displayStyle: str, 需要呈现的模式, 可选项, ['default', 'bold', 'italic', 'underline', 'reverse'], default, "default"
	:param _fontColor: str, 字体颜色, 可选项, ['white', 'red', 'green', 'yellow', 'blue', 'purple', 'grey'], default, "white"
	:param _backColor: str, 背景色, 可选项, ['white', 'red', 'green', 'yellow', 'blue', 'purple', 'grey'], default, None
	:param _prefix: str, 前缀
	:param _suffix: str, 后缀
	:returns: e.g printWithColor("11111111111111", _displayStyle='bold', _fontColor='red', _backColor='grey')
	"""
	displayDict = ['default', 'bold', '-', 'italic', 'underline', '-', '-', 'reverse', '-']
	fontDict = ['white', 'red', 'green', 'yellow', 'blue', 'purple', '-', 'grey']
	backDict = ['white', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'grey']
	if _backColor:
		_display = str(displayDict.index(_displayStyle))
		_font = "3" + str(fontDict.index(_fontColor))
		_back = "4" + str(backDict.index(_backColor))
		print(_prefix + "\033[" + _display + ";" + _font + ";" + _back + "m" + _msg + "\033[0m" + _suffix)
	else:
		_display = str(displayDict.index(_displayStyle))
		_font = "3" + str(fontDict.index(_fontColor))
		print(_prefix + "\033[" + _display + ";" + _font + "m" + _msg + "\033[0m" + _suffix)


def mapminmax(_inputData: pd.DataFrame, _scalerMin: list, _scalerMax: list) -> pd.DataFrame:
	"""
	通过如下方式对数据进行标准化

	:math:`res = \\dfrac{ \\vec{v} - min }{ max - min }`

	:param _inputData: dataframe, 需要进行标准化的数据，列为维度，行为样本
	:param _scalerMax: list, 用于进行标准化的各维度最大值
	:param _scalerMin: list, 用于进行标准化的各维度最小值
	:return: dataframe, 标准化后的数据，列为维度，行为样本，columns名称与输入的_inputData的列名称
	"""
	_dataColumns = _inputData.columns
	_cache = np.divide(np.subtract(_inputData.values, _scalerMin), np.subtract(_scalerMax, _scalerMin))
	_output = pd.DataFrame(_cache, columns=_dataColumns)
	return _output.reset_index(drop=True)


def moduleOfDataframe(_dataframe: pd.DataFrame) -> np.array:
	"""
	计算一个dataframe所表达的多个向量的模

	:param _dataframe: dataframe, 需要进行模计算的数据表，列为维度，行为样本
	:return: np.array, 模
	"""
	return np.sqrt(np.sum(np.matmul(np.asmatrix(_dataframe.values), np.transpose(_dataframe.values)), axis=0))


def cosineThetaOfVectors(_vector01: pd.DataFrame, _vector02: pd.DataFrame) -> list:
	"""
	计算向量1（或多个向量1）与向量2的夹角余弦

	:param _vector01: dataframe, 需要进行夹角计算的向量1，列为维度，行为样本，可以为多个样本
	:param _vector02: dataframe, 需要进行夹角计算的向量2，列为维度，行为样本，必须为单一样本
	:return: list，向量1（或多个向量1）与向量2的夹角余弦
	"""
	_matmul = np.matmul(np.asmatrix(_vector01.values), np.transpose(_vector02.values))
	_vector01_mod = moduleOfDataframe(_vector01)
	_vector02_mod = moduleOfDataframe(_vector02)
	_matmul_mod = np.matmul(_vector01_mod.transpose(), _vector02_mod).transpose()
	_cosineTheta = np.divide(_matmul.transpose(), _matmul_mod).flatten().tolist()[0]
	return _cosineTheta


def randomGrouping(**kwargs):
	"""
	根据比例随机取得一数据表中的样本

	:param _inputX: dataframe, 需要进行分组的对象, 命名必须从_input0开始，如_input1， _input2...
	:param _groupPercentage: float, 分组比例, , default, -1
	:return: None
	"""
	_input0 = kwargs['_input0']
	_group2ndPercentage = kwargs['_group2ndPercentage']
	_quant = kwargs['_input0'].shape[0]
	_output = {}
	# 生成随机矩阵 #
	_group2_locs = sorted(list(np.random.choice(np.arange(_quant), int(np.around(_quant * _group2ndPercentage)))))
	_group1_locs = []
	for item in np.arange(_quant):
		if item not in _group2_locs:
			_group1_locs.append(item)
	for i in range(len(kwargs.keys()) - 1):
		_keyName = '_input' + str(i)
		comStr = '_input' + str(i) + '_group2 = kwargs["' + _keyName + '"].iloc[_group2_locs, :]'
		exec(comStr)
		comStr = '_input' + str(i) + '_group1 = kwargs["' + _keyName + '"].iloc[_group1_locs, :]'
		exec(comStr)
		_outputCache = {'_input' + str(i) + '_group2': locals()['_input' + str(i) + '_group2'],
		                '_input' + str(i) + '_group1': locals()['_input' + str(i) + '_group1']}
		_output = {**_output, **_outputCache}
	return _output

