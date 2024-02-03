# Cài googletrans (api): pip3 install googletrans
# Cài thư viện Pillow
import googletrans
from googletrans import Translator  # Giúp dịch ngôn ngữ, dùng thể hiện của lớp để gọi phương thức

t = Translator()
a = t.translate("Em dep qua", dest="en", src="vi")
print(a.text)