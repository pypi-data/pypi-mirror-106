import sys,click

@click.command()
@click.option('-x', '--xmindpath', 'xmindpath', required=True, help='xmind file path')
@click.option('-e', '--excelpath', 'excelpath', required=True, help='excel file path')
@click.option('-i', '--ignorelayer', 'ignorelayer', is_flag=True, default='0')
def test(xmindPath, excelPath, ignorelayer):
    print(xmindPath + 'haha' + excelPath + 'haha' + ignorelayer)
    # if ignorelayer == '0':
    #     ConvertXmindToExcel().convert(xmindPath, excelPath)
    # else:
    #     ConvertXmindToExcel().convert(xmindPath, excelPath, ignorelayer)
    sys.exit()