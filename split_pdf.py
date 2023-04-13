import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_directory, split_count):
    # 创建输出目录，如果不存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 读取输入 PDF 文件
    with open(input_pdf, 'rb') as f:
        reader = PdfReader(f)

        # 获取 PDF 文件的总页数
        num_pages = len(reader.pages)

        # 计算每个分割文件的页数
        pages_per_split = num_pages // split_count
        if num_pages % split_count != 0:
            pages_per_split += 1

        # 遍历 PDF 文件，按分割数分割
        for i in range(split_count):
            # 创建一个新的 PDF 写入对象
            writer = PdfWriter()

            # 将当前分割的页面添加到新的 PDF 文件中
            for j in range(pages_per_split):
                page_index = i * pages_per_split + j
                if page_index < num_pages:
                    writer.add_page(reader.pages[page_index])

            # 创建输出文件名
            output_file = os.path.join(output_directory, f'output_{i + 1}.pdf')

            # 将新创建的 PDF 文件写入磁盘
            with open(output_file, 'wb') as output:
                writer.write(output)

            print(f'Split {i + 1} saved as {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python split_pdf.py input_pdf output_directory split_count')
    else:
        input_pdf = sys.argv[1]
        output_directory = sys.argv[2]
        split_count = int(sys.argv[3])
        split_pdf(input_pdf, output_directory, split_count)

