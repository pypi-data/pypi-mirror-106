import sys,click

@click.command()
@click.option('-x', '--xmindpath', 'xmindpath', required=True, help='xmind file path')
@click.option('-e', '--excelpath', 'excelpath', required=True, help='excel file path')
@click.option('-i', '--ignorelayer', 'ignorelayer', required=False, default='0')
def test(xmindpath, excelpath, ignorelayer):
    print(xmindpath + 'haha' + excelpath + 'haha' + ignorelayer)
    # if ignorelayer == '0':
    #     ConvertXmindToExcel().convert(xmindPath, excelPath)
    # else:
    #     ConvertXmindToExcel().convert(xmindPath, excelPath, ignorelayer)
    sys.exit()