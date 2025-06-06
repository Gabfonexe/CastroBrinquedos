<template>

  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">


  <div v-if="loading === true" class="min-h-screen flex flex-col items-center justify-center bg-white">
  <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-blue-400 text-3xl font-bold mb-6 animate-pulse animate-bounce">
    Castro Brinquedos
  </span>

  <ProgressSpinner
    style="width: 100px; height: 100px"
    strokeWidth="6"
    fill="transparent"
    animationDuration="0.9s"
    aria-label="Custom ProgressSpinner"
  />

</div>

  <div  v-if="loading===false" class="app-container">

    <Toast /> 
    <MenuTopBar />
  
  <section class="bg-gradient-to-br from-blue-50 to-white py-16 px-6 sm:px-12">
    <div class="max-w-4xl mx-auto text-center">
      <h1 class="text-1xl sm:text-3xl text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-blue-600 text-xl font-bold p-1 animate-bounce animate-pulse mb-20">
        Bem-vindo à página de orçamento
      </h1>
      

      <div class="bg-white p-6 rounded-xl shadow-md max-w-xl mx-auto">
        <p class="text-gray-800 mb-4">
          Está com dúvidas sobre como funciona o processo?
        </p>
        <Button 
          label="Mais Informações" 
          icon="pi pi-info-circle" 
          @click="openPosition('top')" 
          severity="primary" 
          class="w-full sm:w-auto" 
        />
      </div>
    </div>

    <Dialog 
      v-model:visible="visible" 
      header="Como funciona o aluguel?" 
      :style="{ width: '30rem' }" 
      :position="position" 
      :modal="true" 
      :draggable="false"
    >
      <div class="text-surface-700 dark:text-surface-200 space-y-4 text-sm leading-relaxed">
        <p>
          Para realizar o aluguel de brinquedos, siga estes passos:
        </p>
        <ol class="list-decimal pl-5 space-y-2">
          <li>Escolha os brinquedos desejados na lista de produtos.</li>
          <li>Selecione a <strong>quantidade</strong> de cada item.</li>
          <li>Escolha a <strong>data do evento</strong> usando o calendário disponível.</li>
          <li>Preencha o formulário de orçamento com:
            <ul class="list-disc pl-5 mt-1">
              <li>Nome completo</li>
              <li>E-mail</li>
              <li>Telefone para contato</li>
              <li>Mensagem adicional (opcional)</li>
            </ul>
          </li>
        </ol>
        <p>
          Após o envio, entraremos em contato para confirmar os detalhes e a disponibilidade.
          <strong class="block mt-2 text-red-600">
            Importante: a reserva só será garantida após a confirmação do pagamento do valor total do pedido.
          </strong>
        </p>
      </div>

      <div class="flex justify-end gap-2 mt-6">
        <Button type="button" label="Fechar" severity="secondary" @click="visible = false" />
      </div>
    </Dialog>
  </section>

      <Carousel
        id="brinquedos"
        :value="products"
        :numVisible="3"
        :numScroll="1"
        :responsiveOptions="[
          { breakpoint: '1024px', numVisible: 2, numScroll: 1 },
          { breakpoint: '768px', numVisible: 2, numScroll: 1 },
          { breakpoint: '480px', numVisible: 1, numScroll: 1 }
        ]"
      >
        <template #item="slotProps">
          <Card
            class="m-12 sm:m-4 rounded-2xl border border-gray-200 h-70 sm:h-210 shadow-lg transition-transform hover:scale-[1.03] bg-white"
          >
          
            <template #header>
              <img
                :src="`https://castrobrinquedos.onrender.com/static/${slotProps.data.image}`"
                :alt="slotProps.data.type"
                class="w-full h-40 sm:h-64 object-cover rounded-t-2xl"
              />
            </template>

            
            <template #title>
              <h3 class="text-base sm:text-lg font-bold text-center text-gray-800 mt-3">
                {{ slotProps.data.type }}
              </h3>
            </template>

            
            <template #content>
              <p class="text-sm text-gray-600 text-center px-3 mt-2 ">
                {{ slotProps.data.description }}
              </p>
              <div class="text-center mt-3 font-semibold text-lg sm:text-xl text-rose-500 h-1 sm:h-10">
                R$ {{ slotProps.data.price }}/dia
              </div>
            </template>

            
            <template #footer>
              <div class="flex flex-col sm:flex-row justify-center items-center gap-3 mt-4 mb-4 px-4 h-14 sm:h-14">
                <Button
                  :icon="isProductSelected(slotProps.data) ? 'pi pi-check' : 'pi pi-plus'"
                  @click="toggleItem(slotProps.data)"
                  :class="[
                    isProductSelected(slotProps.data)
                      ? 'p-button-success p-button-outlined'
                      : 'p-button-success'
                  ]"
                  class="w-10 h-10 p-0 flex items-center justify-center rounded-full"
                />

                <InputText
                  v-model="slotProps.data.selectedQuantity"
                  type="number"
                  :min="1"
                  :max="slotProps.data.static_quantity"
                  placeholder="Qtd"
                  class="w-4 sm:w-3 h-6 sm:h-9 text-center border border-gray-300 rounded-md"
                  @input="validateQuantity(slotProps)"
                  @blur="validateQuantity(slotProps)"
                />
              </div>
            </template>
          </Card>
        </template>
      </Carousel>

      
    <FormAndCalendar />     
    <FAQ />
    
    <footer class="footer bg-primary text-white text-center py-4">
      <p>Castro Brinquedos &copy; {{ new Date().getFullYear() }}</p>
    </footer>

    <Dialog v-model:visible="showContactDialog" modal header="Contato" :style="{ width: '90vw', maxWidth: '500px' }">
      <div class="p-fluid">
        <div class="field">
          <label for="name">Nome</label>
          <InputText id="name" v-model="contactForm.name" />
        </div>
        <div class="field">
          <label for="email">Email</label>
          <InputText id="email" v-model="contactForm.email" />
        </div>
        <div class="field">
          <label for="phone">Celular</label>
          <InputText id="phone" v-model="contactForm.phone" />
        </div>

        <div class="field">
          <label for="message">Mensagem</label>
          <Textarea id="message" v-model="contactForm.message" rows="3" />
        </div>
      </div>
      <template #footer>
        <Button label="Cancelar" class="p-button-text" @click="showContactDialog = false" />
        <Button label="Enviar" @click="submitContactForm" />
      </template>
    </Dialog>
    <FooterBar />
  </div>
</template>

<script>
import DataView from 'primevue/dataview';
import Timeline from 'primevue/timeline';
import Calendar from 'primevue/calendar';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Card from 'primevue/card';
import Carousel from 'primevue/carousel';
import Toast from 'primevue/toast';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
import axios from 'axios';
import MenuTopBar from './components/MenuTopBar.vue';
import FooterBar from './components/FooterBar.vue';
import FormAndCalendar from './components/FormAndCalendar.vue';
import FAQ from './pages/FAQ.vue';
import { useAmountStore } from './store';
import { mapState, mapWritableState } from 'pinia';
import ProgressSpinner from 'primevue/progressspinner';




export default {
  name: 'App',
  components: {
    Timeline,
    DataView,
    Calendar,
    Dialog,
    Button,
    InputText,
    Textarea,
    Card,
    Carousel,
    Toast,
    Accordion,
    AccordionTab,
    MenuTopBar,
    FooterBar,
    FormAndCalendar,
    FAQ,
    ProgressSpinner,

  },
  data() {
    
    return {
      navigation: [
      { name: 'Product', href: '#' },
      { name: 'Features', href: '#' },
      { name: 'Marketplace', href: '#' },
      { name: 'Company', href: '#' },
      ],
      mobileMenuOpen: false,
      position: 'center',
      visible: false,
      deleteItem: '',
      layout: 'grid',
      options: ['list', 'grid'],
      ProductSelected: false,
      showContactDialog: false,
      selectedProducts: [],
      products: [],
      productsConst: [],
      quantityMap: {},
      loading: true,
    };
  },
  methods: {
     validateQuantity(product) {
      const val = parseInt(product.data.selectedQuantity);
      const max = product.data.static_quantity;

      if(product.data.selectedQuantity > product.data.static_quantity){


              this.$toast.add({
                severity: 'error',
                summary: 'Importante',
                detail:  `O Brinquedo: `+ product.data.type + ` possui o máximo de `  + product.data.static_quantity + ` unidade(s) disponíveis`,
                life: 5000,
              })
              
            }

      if (val === null || val === '') return;

      if (val < 1) product.data.selectedQuantity = 1;
      else if (val > max) product.data.selectedQuantity = max;

      const selected = this.selectedProducts.find(p => p.id === product.data.id);

      if(selected && selected.selectedQuantity !== product.data.selectedQuantity){
        this.selectedProducts = this.selectedProducts.filter(p => p.id !== product.data.id);
      }
    },
    beforeContactForm(){
      this.$toast.add({
          severity: 'info',
          summary: 'Importante',
          detail: `Por favor, adicione algum brinquedo para poder seguir para o formulário de orçamento.`,
          life: 5000,
        });
    },
    openPosition(pos) {
            this.position = pos;
            this.visible = true;
    },
    
    toggleItem(product) {

      const index = this.selectedProducts.findIndex(p => p.id === product.id);
      if (index > -1) {

        this.selectedProducts.splice(index, 1);
        this.ProductSelected = false; 
        const deleteDate = this.disabledDates.filter(item => item.product_type === product.type);
        deleteDate.forEach((item) => {
          

          this.disabledDates.pop(item.product_type);

        })


      } else {
        if(product.selectedQuantity === 0){return}
        this.selectedProducts.push(product);
        this.ProductSelected = true;
        
     
      }

      let totalAmount = 0.0;
      this.selectedProducts.forEach((product) => {
        totalAmount += product.price;
      });
      this.amount = totalAmount;
      this.storeProducts = this.selectedProducts;

      if (this.ProductSelected) {
        for (let p of this.disableDates) {
          const productsFiltered = this.productsConst.filter(item => item.type === p.product)

          if (p.product === product.type) { 

            if(productsFiltered[0].static_quantity - product.selectedQuantity === 0){
       
              const date = new Date(p.date);
              date.setHours(0, 0, 0, 0);
              let objDate = {'date': date, 'product_type': product.type}
              this.disabledDates.push(objDate);
              
            }
            
          }
        }
      } else {
        
        this.deleteItem = this.disabledDates.filter(item => item.product_type === product.type);
        

      }
    },

    isProductSelected(product) {
      return this.selectedProducts.some(p => p.id === product.id);
    },
    
    
  },
  watch:{
    products:{
      handler(newProducts){
        newProducts.forEach((product) => {
          const previusQuantity = this.quantityMap[product.id];
          if (product.selectedQuantity !== previusQuantity){
          this.quantityMap[product.id] = product.selectedQuantity;
          this.toggleItem(product);
        } 
        });
      },
      deep: true
    }
    
  },
  computed: {
    ...mapState(useAmountStore, [
        'disableDates'
      ]),

    ...mapWritableState(useAmountStore, ['amount', 'storeProducts', 'disabledDates']),

  },

  async beforeMount(){
    this.products = (await axios.get('https://castrobrinquedos.onrender.com/products')).data;
    this.products = this.products.map(product => ({
      ...product,
      selectedQuantity: 0
    }));
    this.productsConst =  [...this.products];
    
    this.products.forEach((product) =>{
      this.quantityMap[product.id] = 0;
    })
  },

  async mounted (){
    let response = null;

    while(!response ||  response.status !== 200){
      try{
        response = await fetch('https://castrobrinquedos.onrender.com/');
        if (response.status === 200){
          this.loading = false;
          break;
        } 
      }
      catch (err) {
      }
      await new Promise(resolve => setTimeout(resolve, 2000));
    } 
  }
  
};
</script>

<style>
body.dark {
  background-color: #1e1e1e;
  color: #f0f0f0;
}
.card,
.p-accordion-tab {
  transition: all 0.3s ease;
}
</style>
