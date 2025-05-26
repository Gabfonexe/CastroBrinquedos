<template>
  <footer class="bg-gray-100 text-gray-700 py-12 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10">

      <!-- Coluna 1: Marca e redes sociais -->
      <div>
        <h3 class="text-2xl font-bold text-primary mb-4">Castro Brinquedos</h3>
        <p class="text-sm leading-relaxed mb-6">
          Transformando festas em parques de diversão desde 2010. <br />
          Qualidade, segurança e alegria garantidas.
        </p>
        <div class="flex gap-4">
          <Button  icon="pi pi-instagram"  severity="secondary" text rounded class="hover:scale-110 transition-transform" aria-label="Instagram" />
          <Button @click="goToWhatsapp" icon="pi pi-whatsapp" severity="success" text rounded class="hover:scale-110 transition-transform" aria-label="Whatsapp" />
          <Button @click="goToFacebook" icon="pi pi-facebook" severity="info" text rounded class="hover:scale-110 transition-transform" aria-label="Facebook" />
        </div>
      </div>

      <!-- Coluna 2: Links rápidos -->
      <div>
        <h3 class="text-2xl font-bold text-primary mb-4">Links Rápidos</h3>
        <ul class="space-y-3 border-l-4 border-primary pl-5">
          <li class="flex items-center gap-2">
            <i class="pi pi-home text-primary"></i>
            <a href="#inicio" class="hover:text-primary-600 transition-colors">Início</a>
          </li>
          <li class="flex items-center gap-2">
            <i class="pi pi-star text-primary"></i>
            <a href="#brinquedos" class="hover:text-primary-600 transition-colors">Brinquedos</a>
          </li>
          <li class="flex items-center gap-2">
            <i class="pi pi-calendar text-primary"></i>
            <a href="#disponibilidade" class="hover:text-primary-600 transition-colors">Disponibilidade</a>
          </li>
          <li class="flex items-center gap-2">
            <i class="pi pi-comments text-primary"></i>
            <a href="#depoimentos" class="hover:text-primary-600 transition-colors">Depoimentos</a>
          </li>
          <li class="flex items-center gap-2">
            <i class="pi pi-question-circle text-primary"></i>
            <a href="#faq" class="hover:text-primary-600 transition-colors">FAQ</a>
          </li>
          <li class="flex items-center gap-2">
            <i class="pi pi-envelope text-primary"></i>
            <a href="#contato" class="hover:text-primary-600 transition-colors">Contato</a>
          </li>
        </ul>
      </div>

      <!-- Coluna 3: Serviços -->
      <div>
        <h3 class="text-2xl font-bold text-primary mb-4">Nossos Serviços</h3>
        <ul class="text-sm space-y-3 pl-1">
          <li class="flex items-center gap-2">🎈 Aluguel de Brinquedos</li>
          <li class="flex items-center gap-2">🎉 Recreação Infantil</li>
          <li class="flex items-center gap-2">🏢 Eventos Corporativos</li>
          <li class="flex items-center gap-2">🏫 Festas Escolares</li>
          <li class="flex items-center gap-2">🎁 Festas Completas</li>
        </ul>
      </div>
    </div>

    <div class="border-t border-gray-300 my-8"></div>

    <div class="text-center text-xs text-gray-500">
      © {{ new Date().getFullYear() }} <span class="font-semibold">Castro Brinquedos</span>. Todos os direitos reservados.
    </div>
    <div class="text-center text-xs text-gray-500">
      <span>Desenvolvido por <strong>Gabriel Fonseca</strong>.</span>
      <a href="mailto:gabrielfonseca.devback@gmail.com" class="text-sm text-xl hover:text-primary">
        <span class="text-sm"> gabrielfonseca.devback@gmail.com </span>
        <i class="pi pi-envelope mr-2" ></i>
        </a>
    </div>
  </footer>
</template>


<script>
import Divider from 'primevue/divider'
import Button from 'primevue/button'



export default {
  name: 'FooterBar',
  components:{
    Divider,
    Button
    
  },


  methods:{

    goToFacebook(){
      window.open('https://instagram.com/castrobrinquedos', '_blank');

    },
    goToInstagram(){
      window.open('https://instagram.com/castrobrinquedos', '_blank');
    },
    goToWhatsapp(){
      window.open('https://wa.me/5521968843651', '_blank');
    },
  }
}

</script>

<style scoped>
footer {
  font-family: 'Roboto', sans-serif;
}
</style>

