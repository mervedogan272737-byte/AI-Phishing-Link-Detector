import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Simüle edilmiş URL veri seti
data = {
    'url': [
        'google.com', 'github.com', 'linkedin.com', 'apple.com', 
        'secure-login-bank.com', 'verify-account-now.net', 'update-paypal-info.org', 'win-free-giftcard.biz'
    ],
    'label': [0, 0, 0, 0, 1, 1, 1, 1]  # 0: Güvenli, 1: Phishing
}

df = pd.DataFrame(data)

# Özellik çıkarımı (TF-IDF)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['url'])
y = df['label']

# Modeli eğitme
model = RandomForestClassifier()
model.fit(X, y)

# Test örneği
test_urls = ['my-secure-bank.com', 'facebook.com']
predictions = model.predict(vectorizer.transform(test_urls))

print("--- AI Phishing Link Detector Results ---")
for url, pred in zip(test_urls, predictions):
    status = "⚠️ PHISHING DETECTED!" if pred == 1 else "✅ SAFE URL"
    print(f"URL: {url} -> {status}")
