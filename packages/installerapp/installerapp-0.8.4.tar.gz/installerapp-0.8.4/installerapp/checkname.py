def return_filename(url):
	format = url.split('/')
	len_format = len(format)
	return format[len_format - 1]