# 🚀 Lộ trình Trở thành Data Engineer (Data Engineer Roadmap)

Chào mừng bạn đến với kho lưu trữ (repository) hướng dẫn toàn diện để trở thành một Data Engineer. Lộ trình này được chia thành 4 giai đoạn cốt lõi, đi từ nền tảng lập trình đến việc xây dựng các hệ thống dữ liệu phân tán và hoàn thiện hồ sơ ứng tuyển.

---

## 📍 Giai đoạn 1: Nền tảng vững chắc (Foundation)

Trọng tâm của giai đoạn này là các công cụ giao tiếp và xử lý dữ liệu cốt lõi.

### 1. Làm chủ Python (Lộ trình 6 tuần)
*   **Tuần 1-2 (Cú pháp cơ bản & Cấu trúc dữ liệu):** Nắm vững cách Python lưu trữ biến, kiểu dữ liệu, vòng lặp, hàm và các cấu trúc dữ liệu quan trọng như Hash maps (Dictionary).
*   **Tuần 3-4 (Thư viện xử lý dữ liệu lõi):** Tập trung toàn lực vào **Pandas** và **NumPy** để đọc/ghi dữ liệu (CSV, JSON), lọc, gom nhóm (groupby), gộp bảng và xử lý giá trị rỗng (null/missing values).
*   **Tuần 5 (Thu thập dữ liệu và API):** Sử dụng thư viện `requests` để gọi API và áp dụng kỹ thuật Web Scraping để thu thập nguồn dữ liệu thô phục vụ quá trình Extract.
*   **Tuần 6 (Viết mã sạch & Xử lý lỗi):** Rèn luyện Clean code và Exception handling (`try...except`, logging) để đảm bảo các Data Pipeline chạy tự động mà không bị gián đoạn.

### 2. Cấu trúc dữ liệu & Thuật toán (DSA)
*   Hiểu rõ độ phức tạp thuật toán (Big O Notation).
*   Áp dụng đúng cấu trúc dữ liệu (Hash maps, Trees, Graphs) để tối ưu hiệu suất xử lý dữ liệu lớn.

### 3. Làm chủ SQL Nâng cao
*   Vượt qua các câu lệnh CRUD cơ bản.
*   Làm chủ Window Functions, CTEs, JOINs, Group By, và Subqueries.
*   Nắm vững kỹ thuật tối ưu hóa truy vấn (Query Optimization).

---

## 📍 Giai đoạn 2: Cơ sở dữ liệu & Mô hình hóa (Storage & Data Modeling)

### 1. Hệ quản trị Cơ sở dữ liệu (Database Systems)
*   Hiểu và phân biệt Use-case giữa RDBMS (PostgreSQL, MySQL) và NoSQL (MongoDB, Redis, Cassandra).
*   Phân biệt hệ thống giao dịch (OLTP) và hệ thống phân tích (OLAP).

### 2. Mô hình hóa dữ liệu (Data Modeling)
*   Nắm bắt các kỹ thuật thiết kế Data Warehouse.
*   Thực hành thiết kế theo các mô hình tiêu chuẩn như Star Schema và Snowflake Schema.

### 3. Quy trình ETL/ELT
*   Hiểu sâu về luồng di chuyển dữ liệu: Trích xuất (Extract), Biến đổi (Transform) và Tải (Load).

---

## 📍 Giai đoạn 3: Hệ thống phân tán & Điều phối (Advanced)

### 1. Chất lượng dữ liệu & Điều phối (Data Quality & Orchestration)
*   **Data Quality:** Thiết lập Data Contracts đảm bảo dữ liệu chuẩn định dạng và không trùng lặp.
*   **Orchestration:** Lên lịch và quản lý luồng dữ liệu tự động bằng các công cụ điều phối (Apache Airflow, Prefect, Dagster).

### 2. Hệ thống phân tán (Distributed Systems)
*   Làm quen với tính toán cụm (Cluster Computing) và xử lý dữ liệu song song.
*   **Batch Processing:** Apache Spark.
*   **Stream Processing:** Apache Kafka.

### 3. Nền tảng Đám mây (Cloud) - *Điểm cộng*
*   Làm quen với các dịch vụ lưu trữ đám mây cơ bản như AWS S3 hoặc Google Cloud Storage.

---

## 📍 Giai đoạn 4: Thực hành & Đóng gói (Action & Portfolio)

### 1. Xây dựng Pet Projects
*   Triển khai 1-2 dự án Data Pipeline End-to-End.
*   *Luồng tham khảo:* Lấy dữ liệu qua API -> Làm sạch bằng Pandas -> Lưu vào PostgreSQL (Docker) -> Trực quan hóa bằng PowerBI/Tableau.

### 2. Tối ưu CV & GitHub
*   **GitHub:** Push toàn bộ source code. Bắt buộc có file `README.md` mô tả kiến trúc, luồng dữ liệu và Tech Stack.
*   **CV hướng dữ liệu (Data-driven CV):** Sử dụng các con số thực tế thay vì mô tả chung chung (Ví dụ: "Tự động thu thập 10.000+ dòng dữ liệu mỗi ngày").

### 3. Ôn luyện Coding Test
*   Luyện tập thuật toán Python và SQL trên LeetCode, HackerRank hoặc StrataScratch.

---

## 📚 Tài liệu tham khảo
Trong suốt quá trình học và triển khai dự án, nếu bạn cần tra cứu thêm các thuật ngữ chuyên ngành, tìm hiểu các ví dụ thực tế hoặc tài liệu lý thuyết nền tảng sâu hơn, hãy kiểm tra các thông tin chi tiết được lưu trữ trong tệp **Data EN**. Đây là nguồn tài liệu đắc lực giúp bạn củng cố kiến thức và giải quyết các vấn đề phức tạp trong quá trình xây dựng Data Pipeline.