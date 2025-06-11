<template>
  <section class="calendar-section py-16 px-1 bg-gradient-to-b from-white to-slate-50" id="disponibilidade">
    <Card class="max-w-6xl mx-auto rounded-2xl shadow-2xl border border-gray-200 bg-white transition-all duration-300 ease-in-out hover:shadow-3xl ">
      <template #content>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 p-6 lg:p-10">

          <div>
            <h2 class="text-1xl sm:text-3xl font-semibold text-gray-700 mb-3">📅 Escolha uma data</h2>
            <div class="border border-gray-300 rounded-xl p-1 sm:p-4 shadow-sm bg-white">
              <Calendar
                v-model="selectedDate"
                :inline="true"
                :minDate="minDate"
                :maxDate="maxDate"
                :disabledDates="newDisableDates"
                class="w-full p-calendar" 
                :locale="pt"
              >
                <template #dateTemplate="{ date }">
                  <div
                    :v-tooltip="'Teste'"

                    class="w-full h-full flex items-center justify-center"
                  >
                    {{ date.day }}
                  </div>
                </template>
              </Calendar>
            </div>
          </div>

          <div>
            <h2 class="text-1xl sm:text-2xl font-bold text-gray-800 mb-3">📩 Solicite seu orçamento</h2>
            <div class="space-y-4">
              <InputText
                placeholder="👤 Nome"
                id="name"
                v-model="this.name"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
                required
              />
              <InputText
                placeholder="📧 Email"
                id="email"
                v-model="this.email"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
              <InputText
                placeholder="📱 Celular"
                id="phone"
                v-model="this.phone"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
              <Textarea
                placeholder="💬 Mensagem"
                id="message"
                v-model="this.message"
                rows="4"
                class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
            </div>

            <div class="flex justify-end gap-2 mt-5">
              <Button 
                label="Cancelar" 
                severity="secondary" 
                @click="cancelForm" 
                class="px-1 py-2 text-sm transition-all duration-300 ease-in-out hover:shadow-md" 
              />
              <Button 
                :label="isSubmitting ? 'Enviando...' : 'Enviar'" 
                icon="pi pi-send" 
                :disabled="isSubmitting" 
                @click="submitContactForm" 
                class="px-4 py-2 text-sm transition-all duration-300 ease-in-out hover:shadow-md" 
              />
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
        Textarea,
        
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
        const response = await axios.get('https://castrobrinquedos.onrender.com/unavailable/dates');

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

          if(!item.product){this.disabledDates.push(obj)};

        });
      },


    computed:{
      ...mapState(useAmountStore, [
        'amount',
        'storeProducts',
        'disabledDates',
      ]),
      ...mapWritableState(useAmountStore, ['disableDates']),

      getTooltip(){
          debugger;
          // const dates =  this.newDisableDates.filter((findDate) => {
          //   findDate.date === date && findDate.product === this.storeProducts.filter((product) => {product === findDate.product});
          // });

          const dates = this.DisableDates.map((item) =>{
            item['reason']; 
          })
          return dates.reason;

        },
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
            if(this.name === '' || this.email === '' || this.phone === ''){
              this.$toast.add({
                severity: 'info',
                summary: 'Dados não informado',
                detail: 'Os dados de Nome, Email e Celular devem ser informados.',
                life: 5000,
              })
              return;
            }
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
            if(this.storeProducts.some(product => product.selectedQuantity > product.static_quantity)){
              this.$toast.add({
                  severity: 'error',
                  summary: 'A quantidade está errada',
                  detail: `O pedido excedeu a quantidade de brinquedos disponíveis.`,
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
            const userData = {
                phone: this.phone,
                date: this.selectedDate,
                amount: this.amount,
                products: this.storeProducts,
                email: this.email,
                name: this.name,
                message: this.message,
            };
            
            const response = axios.post('https://castrobrinquedos.onrender.com/criar', userData);
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