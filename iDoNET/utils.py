
def get_alert_box(msg,request):
	html = '''
    <script>
        alert('{}');
        document.location.href = '{}'
    </script>
    '''.format(msg,"").format(request.META.get('HTTP_REFERER'))
	return html