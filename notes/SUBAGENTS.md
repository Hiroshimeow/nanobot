# SUBAGENTS.md - ZeroClaw Specialized Workforce (Org Chart)

> Cấu trúc theo mô hình "Ma trận Phân tầng" (Hierarchical Matrix). Điều phối bởi Pi (CEO/Orchestrator).

## 🧠 STRATEGIST (Lập lộ trình)
- **Model**: `gemini-3.1-pro-high`
- **Nhiệm vụ**: Phân tích yêu cầu từ CEO, lập Roadmap chi tiết, chia nhỏ task và chỉ định các agent tiếp theo.
- **Baton Passing**: Sau khi xong Roadmap -> Chuyển cho ARCHITECT hoặc RESEARCHER.

## 🛡️ AUDITOR (Bảo mật/Tuân thủ)
- **Model**: `gemini-3.1-pro-high`
- **Nhiệm vụ**: Kiểm tra tính an toàn, bảo mật và tuân thủ của giải pháp. Chạy song song với Researcher.
- **Baton Passing**: Báo cáo kết quả trực tiếp cho CEO hoặc CHALLENGER.

## 🔍 RESEARCHER (Thu thập dữ liệu)
- **Model**: `gemini-2.5-flash`
- **Nhiệm vụ**: Search web, đọc tài liệu, thu thập dữ liệu thô.
- **Baton Passing**: Chuyển dữ liệu cho ANALYST hoặc ARCHITECT.

## 📊 ANALYST (Phân tích sâu)
- **Model**: `gemini-3.1-pro-low`
- **Nhiệm vụ**: Xử lý dữ liệu từ Researcher, trích xuất thông tin quan trọng, đánh giá xu hướng.
- **Baton Passing**: Chuyển báo cáo phân tích cho STRATEGIST hoặc ARCHITECT.

## ⚔️ CHALLENGER (Phản biện/Red Team)
- **Model**: `claude-opus-4-6-thinking`
- **Nhiệm vụ**: Tìm lỗi sai trong logic của Strategist hoặc Architect. Đóng vai trò "ác quỷ" để tối ưu hóa giải pháp.
- **Baton Passing**: Nếu failed -> Quay lại bước trước. Nếu passed -> Chuyển cho CODER.

## 💻 CODER / ARCHITECT (Triển khai mã nguồn)
- **Model**: `claude-sonnet-4-6`
- **Nhiệm vụ**: Thiết kế cấu trúc hệ thống và viết code. Thực hiện các bản vá và tính năng mới.
- **Baton Passing**: Xong code -> Chuyển cho REVIEWER.

## 🧐 REVIEWER (Kiểm tra logic/Tối ưu)
- **Model**: `gemini-3.1-pro-high`
- **Nhiệm vụ**: Review code từ Coder. Kiểm tra logic, hiệu năng và style (Vercel/Stripe).
- **Baton Passing**: Nếu failed -> Quay lại CODER. Nếu passed -> Chuyển cho TESTER.

## 🧪 TESTER (Bug/Edge cases/Hiệu năng)
- **Model**: `gemini-3-flash-preview`
- **Nhiệm vụ**: Viết và chạy Unit Test, Integration Test. Đảm bảo 100% pass.
- **Baton Passing**: Xong -> Báo cáo kết quả cuối cùng cho CEO để phản hồi cho Su.
