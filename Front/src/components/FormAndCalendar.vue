<template>
  <section class="calendar-section py-16 px-4 bg-gradient-to-b from-white to-slate-50">
    <Card class="max-w-6xl mx-auto rounded-2xl shadow-2xl border border-gray-200">
      <template #content>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 p-6 lg:p-10">


          <div>
            <h2 class="text-3xl font-bold text-gray-800 mb-6">📅 Escolha a data do seu evento</h2>
            <div class="rounded-xl border border-gray-200 p-1 shadow-sm bg-white" style="width: auto;">
              <Calendar
                v-model="selectedDate"
                :inline="true"
                :minDate="minDate"
                :maxDate="maxDate"
                :disabledDates="newDisableDates"
                class="w-full p-calendar"
                :locale="pt"
                
              />
            </div>
          </div>


          <div>
            <h2 class="text-3xl font-bold text-gray-800 mb-6">📩 Solicite seu orçamento</h2>
            <div class="space-y-4">
              <InputText
                placeholder="Nome"
                id="name"
                v-model="this.name"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
              <InputText
                placeholder="Email"
                id="email"
                v-model="this.email"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
              <InputText
                placeholder="Celular"
                id="phone"
                v-model="this.phone"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
              <Textarea
                placeholder="Mensagem"
                id="message"
                v-model="this.message"
                rows="4"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
            </div>

            <div class="flex justify-end gap-3 mt-6">
              <Button label="Cancelar" severity="secondary" @click="cancelForm" class="px-5 py-2 text-sm" />
              <Button label="Enviar" icon="pi pi-send" @click="submitContactForm" class="px-5 py-2 text-sm" />
            </div>
          </div>

        </div>
      </template>
    </Card>
  </section>
</template>



<script>

import Card from 'primevue/card';
import Button from 'primevue/button';
import Calendar from 'primevue/calendar';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import axios from 'axios';
import { mapState } from 'pinia';
import { mapWritableState } from 'pinia';
import { useAmountStore } from '../store';
import { detail, summary } from '@primeuix/themes/aura/toast';


export default{

    name:'FormAndCalendar',
    components:{
        Card,
        Button,
        Calendar,
        InputText,
        Textarea
    },

    data(){
        const today = new Date();
        const nextYear = new Date();
        nextYear.setFullYear(today.getFullYear() + 1);

        return{
          
            name: '',
            email: '',
            phone: '',
            message: '',
            selectedDate: null,
            minDate: today,
            maxDate: nextYear,
            newDisableDates: [],
        }
    },
    async beforeCreate() {
        const response = await axios.get('http://localhost:8080/unavailable/dates');

        const months = {
          Jan: 0, Feb: 1, Mar: 2, Apr: 3, May: 4, Jun: 5,
          Jul: 6, Aug: 7, Sep: 8, Oct: 9, Nov: 10, Dec: 11
        };

        response.data.forEach((item) => {
          const parts = item.date.split(' '); 
          const day = parseInt(parts[1], 10);
          const month = months[parts[2]];
          const year = parseInt(parts[3], 10);

          const convertDate = new Date(year, month, day); 
          

          const obj = { date: convertDate, product: item.product };
          this.disableDates.push(obj);

        });
      },


    computed:{
      ...mapState(useAmountStore, [
        'amount',
        'storeProducts',
        'disabledDates',
      ]),
      ...mapWritableState(useAmountStore, ['disableDates']),
    },
    watch:{
      disabledDates: {
        handler(val){
          this.newDisableDates = val.map(item => item['date']);
        },
        immediate: true,
        deep: true
      }    
    },

    methods:{
        cancelForm(){
            this.name = '';
            this.email = '';
            this.phone = '';
            this.amount = '';
            this.message = '';
        },
        submitContactForm() {
            console.log('disabledDates: ', this.disabledDates);
            debugger;
            if(this.storeProducts.some(product => 
              product.selectedQuantity === 0 )){
                this.$toast.add({
                  severity: 'info',
                  summary: 'Selecione a Quantidade',
                  detail: `É necessário escolher a quantidade do brinquedo.`,
                  life: 5000,
                })
                return
              }

            if(this.selectedDate === null || this.storeProducts.length === 0){
                if(this.storeProducts.length === 0){
                  this.$toast.add({
                      severity: 'info',
                      summary: 'Selecione um Brinquedo',
                      detail: `É necessário escolher pelo menos 1 brinquedo.`,
                      life: 5000,
                  })        
                }
                else if(this.selectedDate === null){               
                    this.$toast.add({
                      severity: 'info',
                      summary: 'Selecione a Data do Evento',
                      detail: `É necessário escolher a data do evento.`,
                      life: 5000,
                  })
                }
                return
            }

            

            // this.amount = this.selectedProducts.reduce((total, produto) => total + produto.price, 0);
            const userData = {
                phone: this.phone,
                date: this.selectedDate,
                amount: this.amount,
                products: this.storeProducts,
                email: this.email,
                name: this.name,
                message: this.message,
            };
            
            const response = axios.post('http://localhost:8080/criar', userData);
            this.cancelForm()

            if(response){
                this.$toast.add({
                severity: 'success',
                summary: 'Sucesso',
                detail: 'Seu pedido foi enviado com sucesso!',
                life: 3000
                });
            }
            else{
                this.$toast.add({
                severity: 'error',
                summary: 'Erro',
                detail: 'Ocorreu um erro ao realizar o envio do formulário.',
                life: 3000
                });
            }
            },
    }
}



</script>