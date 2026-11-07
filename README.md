# Python AI 80 ngày — code theo video

[![Kiểm code theo video](https://github.com/duonghuyhieu/hoc-python-ai/actions/workflows/kiem.yml/badge.svg)](https://github.com/duonghuyhieu/hoc-python-ai/actions/workflows/kiem.yml) [![Mở bằng Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/duonghuyhieu/hoc-python-ai)

Code của từng video trong series «Python AI 80 ngày» trên kênh **Hiếu học mỗi ngày**. Mỗi ngày một thư mục: README ghi bạn học gì, từng đoạn code trên video kèm lệnh chạy và kết quả máy đã chạy thật, câu đố, đáp án câu đố hôm trước và bài tập. Mỗi tuần máy tự chạy lại toàn bộ code để chắc vẫn ra đúng như video.

## Cách học

```bash
git clone https://github.com/duonghuyhieu/hoc-python-ai.git
cd hoc-python-ai
```

1. Xem video ngày N, mở thư mục `ngay-01`… đọc README, chạy từng file.
2. Làm bài trong thư mục `bai-lam/` (git bỏ qua thư mục này): chép thư mục ngày sang đó rồi sửa, vd `bai-lam/ngay-05/`. Đừng sửa thẳng file trong thư mục ngày.
3. Có video mới: `git pull` — vì bài của bạn nằm trong `bai-lam/` nên không bao giờ bị xung đột.

Không dùng git: nút **Code → Download ZIP**. Không muốn cài gì: nút **Mở bằng Codespaces** ở trên (chạy trên trình duyệt, tài khoản GitHub miễn phí có khoảng 60 giờ mỗi tháng).

## Cài đặt

Python 3.12 (python.org). Mỗi máy làm một lần:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Chạy bài: `python ngay-01/buoc_1.py`.

Tới phần mạng nơ-ron (PyTorch) mới cần torch. Máy không có card NVIDIA nên cài bản CPU cho nhẹ:

```bash
pip install -r requirements-torch.txt --index-url https://download.pytorch.org/whl/cpu
```

## Lộ trình

5/80 ngày đã có video.

| Ngày | Bài | Code |
|---:|---|---|
| 0 | Giới thiệu khóa Python AI 80 ngày | [✅ ngay-00](ngay-00/) |
| | **1. Python cho người đã biết code** | |
| 1 | Python khác gì ngôn ngữ bạn biết | [✅ ngay-01](ngay-01/) |
| 2 | Số trong Python | [✅ ngay-02](ngay-02/) |
| 3 | Chuỗi & list | [✅ ngay-03](ngay-03/) |
| 4 | dict, tuple, set | [✅ ngay-04](ngay-04/) |
| 5 | Comprehension | [✅ ngay-05](ngay-05/) |
| 6 | Hàm | ⏳ sắp có |
| 7 | sorted, lambda, enumerate, zip | ⏳ sắp có |
| 8 | Generator & yield | ⏳ sắp có |
| 9 | Exception | ⏳ sắp có |
| 10 | Class và @dataclass | ⏳ sắp có |
| 11 | Kế thừa | ⏳ sắp có |
| 12 | collections | ⏳ sắp có |
| 13 | MINI | ⏳ sắp có |
| | **2. NumPy** | |
| 14 | ndarray | ⏳ sắp có |
| 15 | Chỉ số & lát cắt mảng 2 chiều | ⏳ sắp có |
| 16 | Lọc bằng mặt nạ boolean | ⏳ sắp có |
| 17 | Broadcasting | ⏳ sắp có |
| 18 | reshape và gộp theo trục | ⏳ sắp có |
| 19 | Số ngẫu nhiên có seed | ⏳ sắp có |
| 20 | Nhân ma trận @ (khác phép * từng phần tử) | ⏳ sắp có |
| | **3. pandas** | |
| 21 | Series | ⏳ sắp có |
| 22 | DataFrame | ⏳ sắp có |
| 23 | Lọc dòng theo điều kiện và query | ⏳ sắp có |
| 24 | Thêm cột tính toán, assign và Copy-on-Write của pandas 3 | ⏳ sắp có |
| 25 | Sắp xếp và đếm | ⏳ sắp có |
| 26 | Dữ liệu thiếu | ⏳ sắp có |
| 27 | Xử lý chữ với .str (dtype str của pandas 3) | ⏳ sắp có |
| 28 | groupby | ⏳ sắp có |
| 29 | merge | ⏳ sắp có |
| | **4. Đọc dữ liệu bằng số** | |
| 30 | Thống kê mô tả | ⏳ sắp có |
| 31 | Biểu đồ bằng chữ | ⏳ sắp có |
| 32 | Tương quan | ⏳ sắp có |
| 33 | ÔN CẤP 1 | ⏳ sắp có |
| 34 | DỰ ÁN CẤP 1 (1/2) | ⏳ sắp có |
| 35 | DỰ ÁN CẤP 1 (2/2) | ⏳ sắp có |
| | **5. Học máy cơ bản** | |
| 36 | Học máy là gì | ⏳ sắp có |
| 37 | Chia train/test | ⏳ sắp có |
| 38 | Đo lỗi hồi quy | ⏳ sắp có |
| 39 | Phân loại (1/2) | ⏳ sắp có |
| 40 | Phân loại (2/2) | ⏳ sắp có |
| 41 | Precision, recall, F1 | ⏳ sắp có |
| 42 | Chuẩn hóa thang đo và k-NN | ⏳ sắp có |
| 43 | Cây quyết định | ⏳ sắp có |
| | **6. Học máy chắc tay** | |
| 44 | Quá khớp | ⏳ sắp có |
| 45 | Cross-validation và GridSearchCV | ⏳ sắp có |
| 46 | Pipeline (1/2) | ⏳ sắp có |
| 47 | Pipeline (2/2) | ⏳ sắp có |
| 48 | Rừng ngẫu nhiên và độ quan trọng của đặc trưng | ⏳ sắp có |
| 49 | Rò rỉ dữ liệu | ⏳ sắp có |
| 50 | Phân cụm KMeans | ⏳ sắp có |
| 51 | ÔN CẤP 2 | ⏳ sắp có |
| 52 | DỰ ÁN CẤP 2 (1/2) | ⏳ sắp có |
| 53 | DỰ ÁN CẤP 2 (2/2) | ⏳ sắp có |
| | **7. Mạng nơ-ron với PyTorch** | |
| 54 | Tensor | ⏳ sắp có |
| 55 | Autograd | ⏳ sắp có |
| 56 | Gradient descent bằng tay | ⏳ sắp có |
| 57 | nn.Module và nn.Linear | ⏳ sắp có |
| 58 | Vòng huấn luyện | ⏳ sắp có |
| 59 | Phân loại bằng mạng | ⏳ sắp có |
| 60 | Mạng nhiều lớp | ⏳ sắp có |
| 61 | Dataset và DataLoader | ⏳ sắp có |
| 62 | train() và eval() | ⏳ sắp có |
| | **8. Ngôn ngữ & embedding** | |
| 63 | Văn bản thành số | ⏳ sắp có |
| 64 | Phân loại văn bản | ⏳ sắp có |
| 65 | Token | ⏳ sắp có |
| 66 | Embedding | ⏳ sắp có |
| 67 | Embedding câu bằng mô hình có sẵn (sentence-transformers) | ⏳ sắp có |
| | **9. Làm việc với LLM** | |
| 68 | LLM là gì | ⏳ sắp có |
| 69 | Gọi API LLM lần đầu với Anthropic SDK | ⏳ sắp có |
| 70 | Prompt tốt | ⏳ sắp có |
| 71 | Structured output | ⏳ sắp có |
| 72 | Tool use (1/2) | ⏳ sắp có |
| 73 | Tool use (2/2) | ⏳ sắp có |
| 74 | RAG (1/2) | ⏳ sắp có |
| 75 | RAG (2/2) | ⏳ sắp có |
| 76 | Agent | ⏳ sắp có |
| 77 | Đánh giá LLM | ⏳ sắp có |
| 78 | ÔN CẤP 3 | ⏳ sắp có |
| | **10. Tốt nghiệp** | |
| 79 | DỰ ÁN CUỐI (1/2) | ⏳ sắp có |
| 80 | DỰ ÁN CUỐI (2/2) | ⏳ sắp có |

## Báo lỗi, hỏi bài

- Code chạy khác video, README sai: [Issues → Báo lỗi bài học](https://github.com/duonghuyhieu/hoc-python-ai/issues/new/choose).
- Hỏi bài, nhờ giải thích: [Discussions](https://github.com/duonghuyhieu/hoc-python-ai/discussions).

## Giấy phép

Code: MIT (`LICENSE`) — dùng thoải mái. Chữ trong README: CC BY 4.0 (`LICENSE-NOI-DUNG.md`) — dùng lại thì ghi công kênh Hiếu học mỗi ngày.
