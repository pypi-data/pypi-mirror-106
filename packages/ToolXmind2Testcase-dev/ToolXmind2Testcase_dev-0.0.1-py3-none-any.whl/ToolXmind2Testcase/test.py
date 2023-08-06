import sys,click
from convert_xmind_to_excel import ConvertXmindToExcel

@click.command()
@click.option('-x', '--xmindpath', 'config', required=True, help='xmind file path')
@click.option('-e', '--excelpath', 'config', required=True, help='excel file path')
@click.option('-i', '--ignorelayer', 'config', is_flag=True, default='0')
# @click.option('--pretty', 'pretty', is_flag=True, default=False, help='pretty print json')
def main(xmindPath, excelPath, ignorelayer):
    test(xmindPath, excelPath, ignorelayer)


def test(xmindPath, excelPath, ignorelayer):
    print(xmindPath + 'haha' + excelPath + 'haha' + ignorelayer)
    # if ignorelayer == '0':
    #     ConvertXmindToExcel().convert(xmindPath, excelPath)
    # else:
    #     ConvertXmindToExcel().convert(xmindPath, excelPath, ignorelayer)
    sys.exit()