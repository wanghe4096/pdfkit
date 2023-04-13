# PDF Splitter

PDF Splitter 是一个简单的 Python 脚本，用于将 PDF 文件分割成指定数量的子文件，每个子文件包含尽可能相等数量的页面。该脚本使用 PyPDF2 库来处理 PDF 文件。

# 环境依赖
确保已安装以下依赖：
```bash
pip install -r requirements.txt
```


# 使用方法
运行以下命令以执行脚本：

```bash
python split_pdf.py input_pdf output_directory split_count

```

- input_pdf 是输入 PDF 文件的路径。
- output_directory 是输出分割文件的目录路径。如果目录不存在，脚本将自动创建。
- split_count 是要将输入 PDF 文件分割成的子文件数量。

# 示例

以下命令将 input.pdf 文件分割为 3 个子文件，每个子文件包含尽可能相等数量的页面。分割文件将保存在 output_directory 中。每个输出文件的文件名格式为 output_<split_number>.pdf。

```bash
python split_pdf.py input.pdf output_directory 3

```

# 注意事项
- 该脚本不会修改原始输入 PDF 文件。
- 请确保在运行脚本之前已安装所有依赖项。
