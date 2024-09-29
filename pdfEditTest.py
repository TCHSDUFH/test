import fitz  # PyMuPDF

def is_blank_page(page):
    """判断页面是否为空白页面（包括图片、矢量图形、文本等）"""
    # 检查文本内容是否为空
    text = page.get_text("text").strip()
    
    # 检查是否存在图片
    image_list = page.get_images(full=True)
    
    # 检查是否有其他绘制元素（比如矩形、矢量图形等）
    drawing_list = page.get_drawings()
    
    # 如果文本为空，且没有图片或其他绘制元素，则认为是空白页
    return len(text) == 0 and len(image_list) == 0 and len(drawing_list) == 0

def add_page_numbers(pdf_path, output_path,fontsize):
    # 打开PDF
    doc = fitz.open(pdf_path)
    total_pages = doc.page_count
    page_number = 1  # 页码从1开始，封面不设置页码

    # if doc.
    #     print('asd')
    # else:
    #     print('df')

    for i in range(total_pages):
        
        page = doc.load_page(i)

        
        # 跳过封面（第一页）
        if i == 0:
            continue

        # 检查当前页面是否为空白页
        if is_blank_page(page):
            continue

        # 设置页码文本框的宽高
        # 如果是恒定的页码位数，那么width = fontsize * （位数 - 2）    至少是* 2
        # 否则直接 字号 * 2
        width = fontsize * 2
        # width = fontsize * 3
        height = fontsize + 3
        
        # 获取页面的高度和宽度，确保正确计算底部的位置
        page_width = page.rect.width
        page_height = page.rect.height
        
        sideGap = 30
        buttonGap = 30

        # 根据当前页的奇偶性决定页码的位置
        if i % 2 != 0:  # 偶数页 -> 反面页，页码放在左下角
            rect = fitz.Rect(sideGap, page_height - buttonGap - height, sideGap + width, page_height - buttonGap)
        else:  # 奇数页 -> 正面页，页码放在右下角
            rect = fitz.Rect(page_width - sideGap - width, page_height - buttonGap - height, page_width - sideGap, page_height - buttonGap)

        # 1. 绘制白色矩形框作为背景
        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

        # 2. 在矩形框中插入页码，黑色字体，设置 overlay=True 以确保页码在最顶层
        page.insert_textbox(rect,
                            str(page_number),
                            fontsize=fontsize,
                            fontname='Times-Roman',    # helv Times-Roman Courier Symbol
                            color=(0.5117953431372549, 0.5787224264705882, 0.7519454656862745),    # 相较于其他的255颜色表示，这里给每位除以255即可
                            align=fitz.TEXT_ALIGN_CENTER,  # 文本居中
                            overlay=True)  # 确保文本在最顶层

        page_number += 1

    # 保存新的PDF
    doc.save(output_path)
    doc.close()



# 使用示例
pdf_path = "C:\\Users\\SDUFH\\Desktop\\pdfAddPage\\32.0-2520-6P01-00使用说明书Operating Instruction（双面打印）.pdf"  # 输入PDF文件路径
output_path = "C:\\Users\\SDUFH\\Desktop\\pdfAddPage\\output1.pdf"  # 输出PDF文件路径
add_page_numbers(pdf_path, output_path,fontsize=26)
