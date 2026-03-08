#!/bin/bash

# Cấu hình
REPO_DIR="/home/ayumi/autonomous_ai/fork"
BRANCH="nnb-linux"
UPSTREAM="upstream"
UPSTREAM_BRANCH="main"
TELEGRAM_CHAT_ID="1182384125"

# Chuyển đến thư mục repo
cd "$REPO_DIR" || exit

# Fetch upstream
git fetch "$UPSTREAM" "$UPSTREAM_BRANCH"

# Thử merge
if git merge --no-commit --no-ff "$UPSTREAM/$UPSTREAM_BRANCH"; then
    # Nếu không có xung đột, commit và đẩy lên
    git commit -m "chore: Auto-merge $UPSTREAM/$UPSTREAM_BRANCH into $BRANCH"
    git push origin "$BRANCH"
    # Gửi thông báo thành công (tùy chọn)
    # nanobot message --content "✅ Đã tự động merge $UPSTREAM/$UPSTREAM_BRANCH vào $BRANCH thành công." --chat_id "$TELEGRAM_CHAT_ID" --channel "telegram"
else
    # Nếu có xung đột, hủy bỏ merge
    git merge --abort
    # Gửi thông báo lỗi
    # nanobot message --content "⚠️ Tự động merge $UPSTREAM/$UPSTREAM_BRANCH vào $BRANCH thất bại do xung đột (conflict). Vui lòng kiểm tra thủ công." --chat_id "$TELEGRAM_CHAT_ID" --channel "telegram"
fi
