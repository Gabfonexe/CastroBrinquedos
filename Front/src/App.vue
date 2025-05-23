<template>

  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  
  
  
  <div class="app-container">
    <!-- index.html ou public/index.html -->

    <Toast />
    
    <MenuTopBar />

    
  
      
  
    
  <section class="bg-gradient-to-br from-blue-50 to-white py-16 px-6 sm:px-12">
    <div class="max-w-4xl mx-auto text-center">
      <h1 class="text-3xl sm:text-4xl font-bold text-blue-900 mb-4">
        Bem-vindo à página de orçamento
      </h1>
      <p class="text-gray-700 text-base sm:text-lg mb-8">
        Aqui você pode alugar brinquedos de forma fácil e rápida! Escolha os produtos, selecione a data, preencha o formulário e aguarde nosso contato. Tudo pensado para garantir diversão com praticidade.
      </p>

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

    <!-- Dialog de Informações -->
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


 

  
       
    <div>
      <template>
          <DataView :value="products" :layout="layout">
              <template #header>
                  <div class="flex justify-end">
                      <SelectButton v-model="layout" :options="options" :allowEmpty="false">
                          <template #option="{ option }">
                              <i :class="[option === 'list' ? 'pi pi-bars' : 'pi pi-table']" />
                          </template>
                      </SelectButton>
                  </div>
              </template>

              <template #list="slotProps">
                  <div class="flex flex-col">
                      <div v-for="(item, index) in slotProps.items" :key="index">
                          <div class="flex flex-col sm:flex-row sm:items-center p-6 gap-4" :class="{ 'border-t border-surface-200 dark:border-surface-700': index !== 0 }">
                              <div class="md:w-40 relative">
                                  <img class="block xl:block mx-auto rounded w-full" :src="`https://primefaces.org/cdn/primevue/images/product/${item.image}`" :alt="item.name" />
                                  <div class="absolute bg-black/70 rounded-border" style="left: 4px; top: 4px">
                                      <Tag :value="item.inventoryStatus"></Tag>
                                  </div>
                              </div>
                              <div class="flex flex-col md:flex-row justify-between md:items-center flex-1 gap-6">
                                  <div class="flex flex-row md:flex-col justify-between items-start gap-2">
                                      <div>
                                          <span class="font-medium text-surface-500 dark:text-surface-400 text-sm">{{ item.category }}</span>
                                          <div class="text-lg font-medium mt-2">{{ item.type }}</div>
                                      </div>
                                      <div class="bg-surface-100 p-1" style="border-radius: 30px">
                                          <div class="bg-surface-0 flex items-center gap-2 justify-center py-1 px-2" style="border-radius: 30px; box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.04), 0px 1px 2px 0px rgba(0, 0, 0, 0.06)">
                                              <span class="text-surface-900 font-medium text-sm">{{ item.rating }}</span>
                                              <i class="pi pi-star-fill text-yellow-500"></i>
                                          </div>
                                      </div>
                                  </div>
                                  <div class="flex flex-col md:items-end gap-8">
                                      <span class="text-xl font-semibold">${{ item.price }}</span>
                                      <div class="flex flex-row-reverse md:flex-row gap-2">
                                          <Button icon="pi pi-heart" outlined></Button>
                                          <Button icon="pi pi-shopping-cart" label="Buy Now" :disabled="item.inventoryStatus === 'OUTOFSTOCK'" class="flex-auto md:flex-initial whitespace-nowrap"></Button>
                                      </div>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>
              </template>

              <template #grid="slotProps">
                  <div class="grid grid-cols-12 gap-4">
                      <div v-for="(item, index) in slotProps.items" :key="index" class="col-span-12 sm:col-span-6 md:col-span-4 xl:col-span-6 p-2">
                          <div class="p-6 border border-surface-200 dark:border-surface-700 bg-surface-0 dark:bg-surface-900 rounded flex flex-col">
                              <div class="bg-surface-50 flex justify-center rounded p-4">
                                  <div class="relative mx-auto">
                                      <img class="rounded w-full" :src="`https://primefaces.org/cdn/primevue/images/product/${item.image}`" :alt="item.type" style="max-width: 300px"/>
                                      <div class="absolute bg-black/70 rounded-border" style="left: 4px; top: 4px">
                                          <Tag :value="item.inventoryStatus"></Tag>
                                      </div>
                                  </div>
                              </div>
                              <div class="pt-6">
                                  <div class="flex flex-row justify-between items-start gap-2">
                                      <div>
                                          <span class="font-medium text-surface-500 dark:text-surface-400 text-sm">{{ item.id }}</span>
                                          <div class="text-lg font-medium mt-1">{{ item.type }}</div>
                                      </div>
                                      <div class="bg-surface-100 p-1" style="border-radius: 30px">
                                          <div class="bg-surface-0 flex items-center gap-2 justify-center py-1 px-2" style="border-radius: 30px; box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.04), 0px 1px 2px 0px rgba(0, 0, 0, 0.06)">
                                              <span class="text-surface-900 font-medium text-sm">{{ item.quantity }}</span>
                                              <i class="pi pi-star-fill text-yellow-500"></i>
                                          </div>
                                      </div>
                                  </div>
                                  <div class="flex flex-col gap-6 mt-6">
                                      <span class="text-2xl font-semibold">${{ item.price }}</span>
                                      <div class="flex gap-2">
                                          <Button icon="pi pi-shopping-cart" label="Buy Now" :disabled="item.inventoryStatus === 'OUTOFSTOCK'" class="flex-auto whitespace-nowrap"></Button>
                                          <Button icon="pi pi-heart" outlined></Button>
                                      </div>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>
              </template>
          </DataView>
          </template>
      </div>
  

      <Carousel :value="products" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions">
          <template #item="slotProps">
            <Card class="m-4 rounded-xl border border-gray-200 shadow-md transition-transform hover:scale-105">
              
              <!-- Imagem do produto -->
              <template #header>
                <img
                  :src="`http://localhost:8080/static/${slotProps.data.image}`"
                  :alt="slotProps.data.type"
                  class="w-full h-64 object-cover rounded-t-xl"
                />
              </template>

              <!-- Título do produto -->
              <template #title>
                <h3 class="text-lg font-bold text-center text-gray-800 mt-4">
                  {{ slotProps.data.type }}
                </h3>
              </template>

              <!-- Descrição e preço -->
              <template #content>
                <p class="text-sm text-gray-600 text-center px-4 mt-2">
                  {{ slotProps.data.description }}
                </p>
                <div class="text-center mt-3 font-semibold text-xl text-rose-500">
                  R$ {{ slotProps.data.price }}/dia
                </div>
              </template>

              <!-- Rodapé com ações -->
              <template #footer>
                <div class="flex justify-center items-center gap-4 mt-4 mb-4 px-4">
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
                    v-model="slotProps.data.quantity"
                    type="number"
                    :min="0"
                    :max="slotProps.data.quantity"
                    placeholder="Qtd"
                    class="w-20 h-10 text-center border border-gray-300 rounded-md"
                  />
                </div>
              </template>
              
            </Card>
          </template>
        </Carousel>


      <div>
        <FormAndCalendar />
      </div>
    
    
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
  </div>
  <FooterBar />
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
import Menubar from 'primevue/menubar';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
import axios from 'axios';
import MenuTopBar from './components/MenuTopBar.vue';
import FooterBar from './components/FooterBar.vue';
import FormAndCalendar from './components/FormAndCalendar.vue';
import FAQ from './pages/FAQ.vue';
import { useAmountStore } from './store';
import { mapState, mapWritableState } from 'pinia';

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
    Menubar,
    Accordion,
    AccordionTab,
    MenuTopBar,
    FooterBar,
    FormAndCalendar,
    FAQ,
  },
  data() {
    
    return {
      position: 'center',
      visible: false,
      deleteItem: '',
      layout: 'grid',
      options: ['list', 'grid'],
      ProductSelected: false,
      showContactDialog: false,
      contactForm: {
        name: '',
        email: '',
        phone: '',
        message: '',
      },
      selectedProducts: [],
      products: [],
      productsConst: [],
      isDark: false,
    };
  },
  methods: {
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
        
        // produto já está selecionado → remover
        this.selectedProducts.splice(index, 1);
        this.ProductSelected = false; 
        debugger;

        const deleteDate = this.disabledDates.filter(item => item.product_type === product.type);
        deleteDate.forEach((item) => {
          this.disabledDates.pop(item.product_type);

        })


      } else {
        // produto não está selecionado → adicionar
        this.selectedProducts.push(product);
        this.ProductSelected = true;
      }

      // Atualiza valor total
      let totalAmount = 0.0;
      this.selectedProducts.forEach((product) => {
        totalAmount += product.price;
      });
      this.amount = totalAmount;
      this.storeProducts = this.selectedProducts;

      // Atualizar datas desabilitadas
      if (this.ProductSelected) {
        
        for (let p of this.disableDates) {
          if (p.product === product.type) { 
            const productsFiltered = this.productsConst.filter(item => item.type === p.product)
            if(productsFiltered[0].quantity - product.quantity === 0){
              
              const date = new Date(p.date);
              date.setHours(0, 0, 0, 0);
              let objDate = {'date': date, 'product_type': product.type}
              // add como obj para poder remover do pop
              this.disabledDates.push(objDate);
              
            }
            
          }
        }
      } else {
        
        this.deleteItem = this.disabledDates.filter(item => item.product_type === product.type);
        

      }
    },

    isProductSelected(product) {
      // const iconElement = buttonElement.querySelector('.pi');
      // if (iconElement.classList.contains('pi-check')) {
      //   this.ProductSelected = true;  

      //   // é o check
      // } else if (iconElement.classList.contains('pi-plus')) {
      //   this.ProductSelected = false;  

      // }
      // this.deleteItem = this.disabledDates.filter(item => item.product === 'Pula Pula Médio');

      // // this.disabledDates.pop(deleteItem);
      return this.selectedProducts.some(p => p.id === product.id);
    },
    
    
  },
  watch:{
    handler(){
    }
  },
  computed: {
    ...mapState(useAmountStore, [
        'disableDates'
      ]),

    ...mapWritableState(useAmountStore, ['amount', 'storeProducts', 'disabledDates']),

    // calculateAmount(){
    //   this.amount = this.selectedProducts.reduce((total, produto) => total + produto.price, 0);
    //   this.products = this.selectedProducts;
    // },


  },


  async beforeMount(){
    this.products = (await axios.get('http://localhost:8080/products')).data;
    this.productsConst = (await axios.get('http://localhost:8080/products')).data;
    // const response = await axios.get('http://localhost:8080/unavailable/dates');

    // this.disabledDates = response.data.map(item => {
      
    //   const date = new Date(item.date);
    //   date.setHours(date.getHours() + 3);
    //   return date
    // });

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
