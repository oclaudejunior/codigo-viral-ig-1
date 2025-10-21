# 🚀 Código Viral IG - Landing Page

Landing page moderna e profissional para o produto digital "Código Viral IG" - 55 Prompts para criar conteúdo viral no Instagram.

## ✨ Características

- **Design Ultra Moderno**: Interface com glassmorphism, animações suaves e efeitos visuais impressionantes
- **Totalmente Responsivo**: Funciona perfeitamente em desktop, tablet e mobile
- **Animações Avançadas**: Cursor customizado, scroll animations, flip cards, e muito mais
- **Integrado com Kiwify**: Checkout pronto para processar pagamentos
- **Performance Otimizada**: Carregamento rápido e experiência fluida
- **SEO Friendly**: Meta tags otimizadas para mecanismos de busca

## 📋 Pré-requisitos

- Python 3.x (para rodar o servidor local)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

## 🚀 Como Usar

### Opção 1: Servidor Python (Recomendado)

1. **Abra o terminal na pasta do projeto**

2. **Execute o servidor:**
   ```bash
   python3 server.py
   ```
   ou
   ```bash
   python server.py
   ```

3. **O navegador abrirá automaticamente** em `http://localhost:8000`

4. **Para parar o servidor:** Pressione `CTRL+C` no terminal

### Opção 2: Abrir Diretamente no Navegador

Simplesmente dê um duplo clique no arquivo `index.html`

**Nota:** Alguns recursos podem não funcionar corretamente devido a restrições de CORS. Use o servidor Python para melhor experiência.

## 📁 Estrutura do Projeto

```
codigo-viral-ig-1/
├── index.html          # Landing page principal
├── server.py           # Servidor local Python
├── prompt-1.png        # Imagens dos exemplos de prompts
├── prompt-2.png
├── prompt-3.png
├── prompt-4.png
├── prompt-5.png
├── prompt-6.png
├── .gitignore
└── README.md
```

## 🎨 Recursos Visuais

### Efeitos Implementados:
- ✅ Cursor customizado com efeito magnético
- ✅ Barra de progresso de leitura
- ✅ Animações de scroll (AOS)
- ✅ Cards com efeito flip 3D
- ✅ Glassmorphism cards
- ✅ Contadores animados
- ✅ Accordion FAQ interativo
- ✅ Partículas flutuantes
- ✅ Gradientes animados
- ✅ Efeitos neon
- ✅ Botões com efeitos shimmer

## 🛠️ Personalização

### Alterar o Link de Checkout

No arquivo `index.html`, localize a linha 898 e altere o link:

```html
<a href="https://pay.kiwify.com.br/SEU-LINK" target="_blank">
```

### Alterar Cores

No arquivo `index.html`, altere as variáveis CSS (linhas 25-31):

```css
:root {
    --orange-primary: #FF6B35;
    --orange-secondary: #F7931E;
    --orange-glow: rgba(255, 107, 53, 0.4);
    --bg-dark: #0a0a0a;
    --bg-elevated: #141414;
}
```

### Alterar Preço

Localize a seção de preços (linha 889-893) e altere os valores:

```html
<p class="text-xl text-gray-400 mb-2">De <s>R$197</s> por apenas</p>
<div class="price-tag">
    <span class="text-7xl font-black neon-text">R$57</span>
</div>
<p class="text-gray-400 mt-2">ou 12x de R$5,70</p>
```

### Substituir Imagens

Substitua os arquivos `prompt-1.png` até `prompt-6.png` pelas suas próprias imagens mantendo os mesmos nomes.

## 🌐 Deploy

### GitHub Pages

1. Faça commit de todas as alterações
2. Push para o GitHub
3. Vá em Settings > Pages
4. Selecione a branch main
5. Salve

Sua página estará disponível em: `https://seu-usuario.github.io/codigo-viral-ig-1`

### Netlify/Vercel

1. Conecte seu repositório GitHub
2. Configure o deploy
3. Pronto! Sua página estará no ar em minutos

## 📊 Seções da Landing Page

1. **Header Fixo**: Navegação com CTA
2. **Hero Section**: Título impactante + CTAs principais
3. **Stats**: Estatísticas em destaque com contadores animados
4. **Features**: 4 cards flip 3D mostrando os benefícios
5. **Transformação**: Antes vs Depois
6. **Benefícios**: 4 razões para comprar
7. **Exemplos Visuais**: Grid com 6 imagens dos prompts
8. **Preço/Checkout**: Oferta com todos os detalhes + garantia
9. **FAQ**: Perguntas frequentes com accordion
10. **CTA Final**: Última chance de conversão
11. **Footer**: Links e copyright

## 🔧 Tecnologias Utilizadas

- **HTML5**: Estrutura semântica
- **CSS3**: Animações e efeitos avançados
- **Tailwind CSS**: Framework CSS utilitário
- **JavaScript Vanilla**: Interatividade e animações
- **AOS (Animate On Scroll)**: Animações de scroll
- **Google Fonts**: Tipografia (Inter + Space Grotesk)

## 📱 Compatibilidade

- ✅ Chrome/Edge (versões recentes)
- ✅ Firefox (versões recentes)
- ✅ Safari (versões recentes)
- ✅ Mobile (iOS/Android)

## 📝 Licença

Este projeto é de uso privado para o produto Código Viral IG.

## 🆘 Suporte

Para dúvidas ou problemas:
1. Verifique se o Python está instalado: `python --version`
2. Certifique-se de estar na pasta correta do projeto
3. Verifique se a porta 8000 está livre
4. Limpe o cache do navegador se houver problemas visuais

## 🎯 Próximos Passos

1. ✅ Teste a página localmente
2. ✅ Verifique todos os links
3. ✅ Teste em diferentes dispositivos
4. ✅ Faça deploy para produção
5. ✅ Configure Google Analytics (opcional)
6. ✅ Configure Facebook Pixel (opcional)

---

**Desenvolvido para converter visitantes em clientes!** 🚀
