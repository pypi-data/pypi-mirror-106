def return_filename(url):
	format = url.split('/')
	len_format = len(format)
	return format[len_format - 1]

def return_filename_without_format(filename):
	file = filename.split('.')
	return file[0]

def return_format(filename):
	format = filename.split('.')
	return format[1]