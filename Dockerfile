# Sử dụng hình ảnh cơ bản từ Superset
FROM apache/superset


# Cài đặt driver MySQL
USER root
RUN pip install mysqlclient
RUN pip install pymysql
# Add other setup commands

# Thêm file cấu hình tùy chỉnh
COPY superset_config.py /app/superset_config.py

# Đảm bảo Superset nhận cấu hình
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Chuyển lại quyền sử dụng cho user superset
USER superset



