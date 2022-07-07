
# 在python3.3之前,只能通过virtualenv创建虚拟环境
# 安装 virtualenv
pip install virtualenv

# 创建虚拟环境
virtualenv --no-site-packages testven_py2

# --no-site-packages:  创建虚拟环境时,不复制主环境中安装的第三方包
# -p:  指定Python解析器
# --no-pip： 不需要安装pip,默认为安装
# --clear： 如果创建虚拟环境的目录已有其他虚拟环境,清除重建

# -------------------------------------------
# 在python3.3之后,可用自带的venv创建虚拟环境

python -m venv testven_py3
# --without-pip:  不需要安装pip,默认为安装
# --clear： 如果创建虚拟环境的目录已有其他虚拟环境,清除重建

