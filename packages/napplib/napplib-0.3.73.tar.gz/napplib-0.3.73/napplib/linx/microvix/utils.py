from lxml import objectify


def add(start = 0):
	i = start
	while True:
		yield i
		i = i + 1


def xml_to_dict_array(xml):
	result = list()

	if not xml:
		raise Exception('Response is empty or None')

	root = objectify.fromstring(xml)

	responseSuccess = str(root.ResponseResult.ResponseSuccess) == 'True'

	if not responseSuccess:
		error_message = root.ResponseResult.ResponseError.Message
		error_message = [ str(item) for item in error_message ]
		error_message = '\n'.join(error_message)
		raise Exception(f'The response failed. Reason: \n\n{error_message}')

	headers = [ str(item) for item in root.ResponseData.C.D ]

	for item in root.ResponseData.R:

		tmp = dict()
		index = add()

		for header in headers:
			tmp[header] = str(item.D[next(index)])

		result.append(tmp)

	return result
