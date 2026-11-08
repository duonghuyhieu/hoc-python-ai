# Python AI 80 ngày — code dự án theo video

[![Kiểm code theo video](https://github.com/duonghuyhieu/hoc-python-ai/actions/workflows/kiem.yml/badge.svg)](https://github.com/duonghuyhieu/hoc-python-ai/actions/workflows/kiem.yml) [![Mở bằng Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/duonghuyhieu/hoc-python-ai)

Code các bài dự án và bài mini trong series «Python AI 80 ngày» trên kênh **Hiếu học mỗi ngày** — những bài code dài, khó gõ lại theo video. Bài thường ngắn, gõ theo video là đủ nên không có ở đây. Mỗi bài một thư mục: README ghi bạn học gì, từng đoạn code trên video kèm lệnh chạy và kết quả máy đã chạy thật, câu đố và bài tập. Mỗi tuần máy tự chạy lại toàn bộ code để chắc vẫn ra đúng như video.

## Cách học

```bash
git clone https://github.com/duonghuyhieu/hoc-python-ai.git
cd hoc-python-ai
```

1. Xem video bài dự án, mở thư mục của ngày đó (vd `ngay-13`), đọc README, chạy từng file.
2. Làm bài trong thư mục `bai-lam/` (git bỏ qua thư mục này): chép thư mục ngày sang đó rồi sửa, vd `bai-lam/ngay-13/`. Đừng sửa thẳng file trong thư mục ngày.
3. Có bài dự án mới: `git pull` — vì bài của bạn nằm trong `bai-lam/` nên không bao giờ bị xung đột.

Không dùng git: nút **Code → Download ZIP**. Không muốn cài gì: nút **Mở bằng Codespaces** ở trên (chạy trên trình duyệt, tài khoản GitHub miễn phí có khoảng 60 giờ mỗi tháng).

## Cài đặt

Python 3.12 (python.org). Mỗi máy làm một lần:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Chạy bài: `python ngay-13/buoc_1.py`.

Tới phần mạng nơ-ron (PyTorch) mới cần torch. Máy không có card NVIDIA nên cài bản CPU cho nhẹ:

```bash
pip install -r requirements-torch.txt --index-url https://download.pytorch.org/whl/cpu
```

## Các bài dự án

0/7 bài đã có code (khóa 80 ngày).

| Ngày | Bài | Code |
|---:|---|---|
| 13 | MINI: báo cáo doanh thu tiệm bánh ngọt bằng Python thuần | ⏳ sắp có |
| 34 | DỰ ÁN CẤP 1 (1/2): đơn hàng livestream — làm sạch dữ liệu | ⏳ sắp có |
| 35 | DỰ ÁN CẤP 1 (2/2): đơn hàng livestream — báo cáo, biểu đồ chữ | ⏳ sắp có |
| 52 | DỰ ÁN CẤP 2 (1/2): hội viên hồ bơi bỏ gói — khám dữ liệu, mốc so sánh | ⏳ sắp có |
| 53 | DỰ ÁN CẤP 2 (2/2): hội viên hồ bơi bỏ gói — mô hình ưu tiên recall | ⏳ sắp có |
| 79 | DỰ ÁN CUỐI (1/2): trợ lý hỏi đáp homestay — truy hồi và chấm | ⏳ sắp có |
| 80 | DỰ ÁN CUỐI (2/2): trợ lý homestay nối LLM | ⏳ sắp có |

## Báo lỗi, hỏi bài

- Code chạy khác video, README sai: [Issues → Báo lỗi bài học](https://github.com/duonghuyhieu/hoc-python-ai/issues/new/choose).
- Hỏi bài, nhờ giải thích: [Discussions](https://github.com/duonghuyhieu/hoc-python-ai/discussions).

## Giấy phép

Code: MIT (`LICENSE`) — dùng thoải mái. Chữ trong README: CC BY 4.0 (`LICENSE-NOI-DUNG.md`) — dùng lại thì ghi công kênh Hiếu học mỗi ngày.
