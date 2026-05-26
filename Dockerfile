# Usa a imagem oficial do n8n
FROM n8nio/n8n:latest

# Copia os workflows para importação automática (opcional)
COPY --chown=node:node "Agente Clinica Inspire — Feegow v3.json" /home/node/workflows/workflow.json

# A porta padrão do n8n é 5678
EXPOSE 5678

# Comando padrão da imagem n8n
CMD ["n8n", "start"]
