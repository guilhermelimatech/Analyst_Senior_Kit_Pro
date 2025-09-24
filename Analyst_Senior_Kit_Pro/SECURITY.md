# Segurança e Boas Práticas

## 🔒 Credenciais
- Em `.env` (não versionar).
- Rotacione chaves.

## 🧩 Dados Sensíveis
- Anonimizar PII (LGPD/GDPR) antes de compartilhar.

## 🛠 Fail-safe & Logs
- Validar schema antes do processamento.
- Em falha, não gerar outputs parciais.
- Log estruturado (INFO/WARN/ERROR).
