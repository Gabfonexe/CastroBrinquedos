<template>
  <section class="faq-section py-12 px-6 bg-yellow-50 max-w-4xl mx-auto rounded-xl shadow-lg">
    <h2 class="text-4xl font-extrabold text-primary text-center mb-8">
      Perguntas Frequentes
    </h2>

    <Accordion :multiple="true" :activeIndex="[0]" class="border border-yellow-200 rounded-lg overflow-hidden shadow-sm">
      <AccordionTab
        v-for="(faq, index) in faqs"
        :key="index"
        :header="faq.question"
        class="border-b border-yellow-200 last:border-b-0"
        header-class="text-lg font-semibold text-yellow-900 bg-yellow-100 hover:bg-yellow-200 transition-colors px-6 py-4 rounded-none"
        content-class="text-yellow-800 px-6 py-4 bg-yellow-50"
      >
        <p>{{ faq.answer }}</p>
      </AccordionTab>
    </Accordion>
  </section>
</template>


<script>
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
export default{
    name:'FAQ',
    components:{
        Accordion,
        AccordionTab
    },
    data(){
        return{
            faqs: [
                { question: 'Com quanto tempo de antecedência preciso reservar?', answer: 'Recomendamos pelo menos 1 semana antes do evento para garantir a disponibilidade.' },
                { question: 'O transporte está incluso no valor?', answer: 'Sim, para eventos dentro da cidade. Fora da cidade pode haver taxa adicional.' },
                { question: 'Como faço o pagamento?', answer: 'Aceitamos PIX, transferência bancária e cartão de crédito.' },
            ],
        }
    }
}

</script>