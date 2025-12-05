import streamlit as st
from pdf2docx import Converter
import os
import time

# 1. 设置网页标题和布局
st.set_page_config(page_title="呆马猪猪·PDF神器", page_icon="🐷")

# 2. 侧边栏 (Sidebar)
with st.sidebar:
    st.title("🐷 呆马猪猪工作室")
    st.info("专注效率工具开发\n\n闲鱼/小红书搜索：呆马猪猪")
    st.markdown("---")
    st.write("本工具永久免费，不限页数！")

# 3. 主界面
st.title("📄 PDF 转 Word 转换器 (Pro版)")
st.write("只需一步，将 PDF 拖入下方，立刻变身可编辑的 Word 文档！")

# 4. 文件上传区
uploaded_file = st.file_uploader("请上传您的 PDF 文件", type="pdf")

if uploaded_file is not None:
    # 显示文件信息
    st.success(f"✅ 已收到文件: {uploaded_file.name}")
    
    # 创建一个按钮
    if st.button("开始转换 (Start)"):
        # 进度条
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Streamlit 处理文件比较特殊，需要先保存到临时文件
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            status_text.text("⏳ 正在解析 PDF 结构...")
            progress_bar.progress(30)
            
            # 开始转换
            docx_file = "converted.docx"
            cv = Converter("temp.pdf")
            cv.convert(docx_file) # 转换核心代码
            cv.close()
            
            progress_bar.progress(100)
            status_text.text("🎉 转换完成！")
            
            # 提供下载按钮
            with open(docx_file, "rb") as file:
                btn = st.download_button(
                    label="📥 点击下载 Word 文档",
                    data=file,
                    file_name=f"{uploaded_file.name}_呆马猪猪转换.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
            st.balloons() # 放个气球庆祝一下！
            
            # 清理临时文件
            os.remove("temp.pdf")
            # os.remove(docx_file) # 下载完再删，这里先留着
            
        except Exception as e:
            st.error(f"❌ 转换失败: {e}")