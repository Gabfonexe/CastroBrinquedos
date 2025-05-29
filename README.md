# ✨ Projeto de Apoio para Empresa de Locação de Brinquedos

Este projeto foi desenvolvido para atender a uma demanda real de mercado, oferecendo uma solução completa para o gerenciamento de uma empresa especializada em locação de brinquedos. Pensado e criado do zero por mim, ele surgiu como resposta à necessidade de um amigo empreendedor e, desde então, tem evoluído continuamente, tornando-se um sistema robusto, escalável e com foco total na usabilidade.

---

## 📊 Tecnologias Utilizadas

### Back-end

* **Python**
* **Flask**
* **SQLAlchemy** (ORM)
* **Marshmallow** (Serialização e validação de dados)
* **Flask-Admin** (Dashboard administrativo)
* **Flask-Migrate** (Controle de versão do banco de dados)
* **PostgreSQL**

### Front-end

* **Vue.js** (Options API)
* **PrimeVue** (Componentes UI modernos e acessíveis)
* **Tailwind CSS** (Estilização responsiva e utilitária)
* **HTML5 & CSS3**
* **JavaScript / TypeScript**

---

## 🛍️ Sobre o Projeto

O sistema foi criado inicialmente como um simples CRUD para controle interno, mas evoluiu para um produto completo com landing page responsiva, painel administrativo, calendário reativo e integração total com banco de dados.

### 🎨 Estrutura do Projeto

#### ✨ Landing Page com Vue.js

A landing page foi criada com **Vue.js** como um desafio pessoal e com foco em escalabilidade e manutenção. A modularização foi uma escolha estratégica, mesmo sendo uma página relativamente simples. Os brinquedos exibidos no carrossel vêm diretamente do banco de dados.

#### 🔎 Integração Back-End e Admin

A API foi estruturada com **Flask**, organizando os módulos de forma clara, performática e extensível. O **Flask-Admin** permite ao cliente editar dados como nome, preço, descrição dos brinquedos, entre outros.

#### 🗓️ Calendário Reativo

Uma das partes mais interessantes é o calendário inteligente, que:

* Mostra datas indisponíveis com base nas reservas existentes.
* Atualiza automaticamente com uma rotina em segundo plano a cada 6 horas.
* Verifica a disponibilidade antes de permitir uma nova reserva.

#### ✉️ Captura de Leads

Um sistema simples de captura de leads foi implementado para coleta de informações de clientes potenciais, com possibilidade futura de integração via Webhooks.

#### 👨‍💻 Painel Administrativo (Flask-Admin)

O painel administrativo oferece:

* Controle total dos produtos e usuários.
* Confirmação de pagamentos e locações.
* Visualização de relatórios dinâmicos e histórico de reservas.

---

## ⚖️ Arquitetura e Lógicas Avançadas

### 💡 Rotina de Sincronização

Foi criada uma rotina backend que:

* Roda a cada 6 horas ou ao receber novo formulário.
* Verifica se um produto alugado foi devolvido ("verificado").
* Atualiza automaticamente o estoque.
* Mantém a performance da consulta ao ignorar itens já processados.
* Registra datas de maior demanda para relatórios futuros.

### 🔄 Migrações com Flask-Migrate

Todas as alterações no banco de dados estão versionadas em `migrations/versions`, permitindo:

* Rollbacks fáceis.
* Diagnóstico e correção de bugs via BugFix.

### 🔐 Controle de Acesso e Autonomia do Cliente

* Alguns campos do modelo são editáveis pelo cliente via painel (como `is_confirmed`).
* O cliente tem autonomia total, mesmo sem conhecimentos avançados em tecnologia.

---

## 🚀 Resultados Alcançados

* Sistema performático, modular e responsivo.
* Escalabilidade garantida com uso de boas práticas.
* Cliente final satisfeito com o controle e autonomia do sistema.

---

## 🌐 Demonstração

> [Castro Brinquedos - Landing Page](https://castro-brinquedos.vercel.app)

> [Castro Brinquedos - Web Service](https://castro-brinquedos-1r7b.vercel.app)

---

## 📖 Considerações Finais

Esse projeto foi uma experiência valiosa tanto tecnicamente quanto pessoalmente. Uni boas práticas de desenvolvimento com uma necessidade real, entregando uma solução moderna, responsiva e eficaz.

Se você gostou do projeto ou quer saber mais, sinta-se à vontade para entrar em contato comigo!

---

**Desenvolvido com ❤️ por \[Gabriel Fonseca]**
