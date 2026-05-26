# Usa a imagem oficial do n8n
FROM n8nio/n8n:latest

# Copia os workflows para importação automática (opcional)
COPY --chown=node:node agente-clinica-inspire-feegow-v3.json /home/node/workflows/workflow.json

