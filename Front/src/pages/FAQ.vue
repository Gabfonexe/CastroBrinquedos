<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Faq',
  data() {
    return {
      activeIndex: 0,
      searchQuery: '',
      items: [
        {
          label: 'Geral',
          icon: 'pi pi-fw pi-info-circle',
          questions: [
            {
              question: 'Há um período de teste?',
              answer:
                'Sim, oferecemos um período de teste gratuito de 30 dias. Após esse período, a cobrança será feita automaticamente no cartão de crédito cadastrado na plataforma.',
            },
            {
              question: 'Preciso me inscrever com cartão de crédito?',
              answer:
                'Sim, é necessário cadastrar um cartão de crédito, pois a cobrança é realizada de forma recorrente no formato de assinatura. O débito será efetuado mensalmente ou anualmente, conforme o plano escolhido.',
            },
            {
              question: 'A assinatura é mensal ou anual?',
              answer: `Oferecemos ambos os formatos: mensal e anual.<br><br><strong>Plano mensal:</strong> O valor da mensalidade é calculado com base no faturamento no momento da assinatura. Caso seu faturamento aumente e ultrapasse a faixa atual, a mensalidade será ajustada automaticamente.<br><br><strong>Plano anual:</strong> O valor é definido com base em uma análise do faturamento no momento da contratação e será mantido fixo durante os 12 meses. Uma nova análise será realizada apenas após 365 dias.`,
            },
            {
              question: 'Como funciona o Plano anual?',
              answer:
                'No plano anual, você recebe um desconto de 30% sobre o valor total e pode parcelar em até 12 vezes. É uma ótima opção para economizar e garantir estabilidade no pagamento.',
            },
            {
              question: 'Quantos níveis existem?',
              answer:
                'Nossos planos se ajustam conforme seu faturamento, com faixas personalizadas para diferentes níveis de vendas.',
            },
            {
              question:
                'É possivel ser Afiliado e ganhar indicando para parceiros?',
              answer:
                'Sim. Temos um canal só para afiliados que será divulgado em breve. Comissões vitalícias e prêmios de metas definidos, para parceiros que indicarem não só o fullfacil como tambem nossos outros aplicativos para vendedores.',
            },
            {
              question: 'O fullfacil tem uma versão gratuita?',
              answer:
                'Sim, as integrações assim como a página home assim e os relatórios mensais que te trazem informações valiosas sobre a gestão full da suas lojas são 100% gratuitos. Você paga apenas pelo acesso a notificações e envios inteligentes',
            },
            {
              question: 'Quais são as faixas de pagamento?',
              answer: `As faixas de pagamento são baseadas no faturamento mensal e estão organizadas da seguinte forma:<br><br>
      - <strong>R$ 0 a R$ 50.000:</strong> R$ 99,80<br>
      - <strong>R$ 50.001 a R$ 100.000:</strong> R$ 199,80<br>
      - <strong>R$ 100.001 a R$ 300.000:</strong> R$ 399,80<br>
      - <strong>R$ 300.001 a R$ 500.000:</strong> R$ 559,80<br>
      - <strong>R$ 500.001 a R$ 1.000.000:</strong> R$ 799,80<br>
      - <strong>R$ 1.000.001 a R$ 2.000.000:</strong> R$ 1.099,80<br>
      - <strong>Acima de R$ 2.000.000:</strong> Valor a consultar`,
            },
          ],
        },
        {
          label: 'Envio de E-mails',
          icon: 'pi pi-fw pi-envelope',
          questions: [
            {
              question: 'Como configuro minha conta?',
              answer:
                'Você pode configurar sua conta acessando a aba de configurações e vinculando seu email preferido.',
            },
            {
              question: 'Existe um limite para o envio de e-mails?',
              answer:
                'O limite depende do seu plano, mas garantimos que a maioria dos usuários não enfrentará restrições.',
            },
            {
              question: 'Qual é o tamanho da minha caixa de entrada?',
              answer:
                'Sua caixa de entrada suporta até 5GB por padrão, com opções de expansão nos planos avançados.',
            },
            {
              question: 'Como posso adicionar anexos?',
              answer:
                'Você pode adicionar anexos de até 10MB diretamente no editor de emails da plataforma.',
            },
            {
              question: 'Como funciona as notificações de alerta?',
              answer:
                'Ao cadastrar seu número na página de notificações você receberá alertas customizados pelo whatsapp até que desative a integração na página ou pelo whatsapp.',
            },
          ],
        },
        {
          label: 'Suporte',
          icon: 'pi pi-fw pi-question-circle',
          questions: [
            {
              question: 'Como posso obter suporte?',
              answer:
                'Entre em contato pelo e-mail: fullfacil@market2ai.com.br ou use o botão "Ajuda e Feedback".',
            },
            {
              question: 'Qual é o tempo de resposta?',
              answer: 'Nosso tempo médio de resposta é de 48h em dias úteis.',
            },
            {
              question: 'Existe um fórum da comunidade?',
              answer:
                'Sim! Temos uma comunidade ativa onde você pode tirar dúvidas e trocar experiências.',
            },
            {
              question: 'O chat ao vivo está disponível?',
              answer:
                'O chat ao vivo está disponível para planos premium e empresariais.',
            },
            {
              question: 'Tenho sugestões de ideias!',
              answer:
                'Somos super aberto a novas ideias dos nossos clientes, utilize os mesmos canais acima que com certeza sua ideia será avaliada. Após avaliado nosso time irá te passar um feedback',
            },
          ],
        },
        {
          label: 'Cobrança',
          icon: 'pi pi-fw pi-credit-card',
          questions: [
            {
              question: 'Receberei uma fatura?',
              answer: 'Sim, você receberá uma fatura detalhada todos os meses.',
            },
            {
              question: 'Como fornecer minhas informações de pagamento?',
              answer:
                'Você pode adicionar ou atualizar suas informações de pagamento diretamente nas configurações da conta.',
            },
            {
              question: 'O IVA está incluído?',
              answer:
                'O IVA está incluído nos preços mostrados, sem custos surpresa.',
            },
            {
              question: 'Posso receber faturas em PDF?',
              answer:
                'Sim, basta ativar a opção "Receber fatura em PDF" nas configurações.',
            },
          ],
        },
      ],
      frequently: [
        {
          frequentlyAsked: [
            {
              question: 'Há um período de teste?',
              answer:
                'Sim, oferecemos um período de teste gratuito de 30 dias. Após esse período, a cobrança será feita automaticamente no cartão de crédito cadastrado na plataforma.',
            },
            {
              question: 'Como funciona o Plano anual?',
              answer:
                'No plano anual, você recebe um desconto de 30% sobre o valor total e pode parcelar em até 12 vezes. É uma ótima opção para economizar e garantir estabilidade no pagamento.',
            },
            {
              question: 'O IVA está incluído?',
              answer:
                'O IVA está incluído nos preços mostrados, sem custos surpresa.',
            },
            {
              question: 'Como posso obter suporte?',
              answer:
                'Entre em contato pelo e-mail: fullfacil@market2ai.com.br ou use o botão "Ajuda e Feedback".',
            },
            {
              question: 'O chat ao vivo está disponível?',
              answer:
                'O chat ao vivo está disponível para planos premium e empresariais.',
            },
            {
              question: 'Existe um fórum da comunidade?',
              answer:
                'Sim! Temos uma comunidade ativa onde você pode tirar dúvidas e trocar experiências.',
            },
          ],
        },
      ],
    };
  },
  computed: {
    filteredFaqs() {
      if (!this.searchQuery || !this.searchQuery.trim()) {
        return null;
      }

      const query = this.searchQuery.toLowerCase().trim();
      const results = [];

      this.items.forEach((category) => {
        category.questions.forEach((item) => {
          if (
            item.question.toLowerCase().includes(query) ||
            item.answer.toLowerCase().includes(query)
          ) {
            results.push({
              category: category.label,
              icon: category.icon,
              ...item,
            });
          }
        });
      });

      return results;
    },
  },
  methods: {
    changeItem(index) {
      this.activeIndex = index;
    },
    clearSearch() {
      this.searchQuery = '';
    },
  },
});
</script>

<template>
  <div>
    <div class="flex flex-col md:flex-row items-center justify-between mb-6">
      <div class="text-900 dark:text-surface-0 font-bold text-2xl mb-4 md:mb-0">
        Perguntas Frequentes
      </div>

      <!-- Campo de Busca Redesenhado -->
      <div class="w-full md:w-96">
        <div
          class="flex p-0 shadow-sm rounded-full overflow-hidden border-2 border-primary"
        >
          <div class="flex items-center justify-center bg-primary w-12 h-14">
            <i class="pi pi-search text-white text-xl"></i>
          </div>
          <InputText
            v-model="searchQuery"
            placeholder="Buscar perguntas frequentes..."
            class="w-full p-inputtext-lg border-0 flex-1"
          />
          <Button
            v-if="searchQuery"
            icon="pi pi-times"
            class="p-button-rounded p-button-text p-0 mr-2 flex items-center"
            @click="clearSearch"
            aria-label="Limpar busca"
          />
        </div>
      </div>
    </div>

    <!-- Resultados da Busca -->
    <div v-if="filteredFaqs && filteredFaqs.length > 0">
      <Card class="mb-4">
        <template #title>
          <div class="flex items-center justify-between">
            <span>Resultados da Busca</span>
            <Badge :value="filteredFaqs.length" severity="info" />
          </div>
        </template>
        <template #content>
          <Accordion>
            <AccordionTab
              v-for="(q, i) in filteredFaqs"
              :key="i"
              :header="q.question"
            >
              <div
                class="mb-2 text-sm text-surface-600 dark:text-surface-400 flex items-center"
              >
                <i :class="q.icon" class="mr-2"></i>
                <span>{{ q.category }}</span>
              </div>
              <p class="m-0 p-0" v-html="q.answer"></p>
            </AccordionTab>
          </Accordion>
        </template>
      </Card>
    </div>

    <!-- Mensagem quando não há resultados -->
    <div
      v-else-if="
        searchQuery &&
        searchQuery.trim() &&
        (!filteredFaqs || filteredFaqs.length === 0)
      "
      class="mb-4"
    >
      <Message severity="info" :closable="false">
        Nenhum resultado encontrado para "{{ searchQuery }}". Tente usar termos
        diferentes.
      </Message>
    </div>

    <!-- Exibição normal quando não há busca -->
    <div v-else class="flex flex-col md:flex-row gap-8">
      <Card class="mb-0 md:w-80">
        <template #title>Categorias</template>
        <template #content>
          <ul class="list-none m-0 p-0">
            <li
              v-for="(item, i) in items"
              :key="i"
              @click="changeItem(i)"
              class="mb-2"
            >
              <a
                class="flex items-center cursor-pointer select-none p-4 transition-colors duration-150 rounded"
                :class="{
                  'bg-primary text-primary-contrast': activeIndex === i,
                  'hover:bg-surface-100 dark:hover:bg-surface-800':
                    activeIndex !== i,
                }"
              >
                <i class="mr-2 text-lg" :class="item.icon"></i>
                <span>{{ item.label }}</span>
              </a>
            </li>
          </ul>
        </template>
      </Card>

      <Card class="flex-1">
        <template #content>
          <Accordion>
            <AccordionTab
              v-for="(q, i) in items[activeIndex].questions"
              :key="i"
              :header="q.question"
            >
              <p class="m-0 p-0" v-html="q.answer"></p>
            </AccordionTab>
          </Accordion>
        </template>
      </Card>
    </div>
  </div>
</template>

<style scoped>
.p-accordion-header {
  font-size: 1.25rem;
  font-weight: 600;
  padding: 1rem;
  background-color: var(--surface-50);
  border-radius: 8px;
  margin-bottom: 0.5rem;
  transition: background-color 0.3s ease;
}

.p-accordion-header:hover {
  background-color: var(--surface-100);
}

.p-accordion-content {
  padding: 1rem;
  background-color: var(--surface-0);
  border-radius: 8px;
  margin-bottom: 0.5rem;
}

.text-900 {
  color: var(--surface-900);
}

.dark .text-surface-0 {
  color: var(--surface-0);
}
</style>
