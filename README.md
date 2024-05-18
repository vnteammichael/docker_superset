# docker_superset

docker-compose up -d  # Khởi động các dịch vụ
docker-compose exec superset superset db upgrade  # Nâng cấp cơ sở dữ liệu
docker-compose exec superset superset fab create-admin  # Tạo tài khoản admin
docker-compose exec superset superset init  # Khởi tạo Superset
