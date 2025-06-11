<template>
  <div class="card">
    <DataView :value="products" :layout="layout">
      <!-- Botão de troca de layout (opcional) -->
      <template #header>
        <div class="flex justify-end mb-4">
          <SelectButton
            v-model="layout"
            :options="['grid']"
            :allowEmpty="false"
          >
            <template #option="{ option }">
              <i :class="[option === 'list' ? 'pi pi-bars' : 'pi pi-table']" />
            </template>
          </SelectButton>
        </div>
      </template>

      <!-- Layout em grade (semelhante ao carousel anterior) -->
      <template #grid="slotProps">
        <div class="grid grid-cols-12 gap-4">
          <div
            v-for="(item, index) in slotProps.items"
            :key="index"
            class="col-span-12 sm:col-span-6 md:col-span-4 xl:col-span-4 p-2"
          >
            <Card
              class="m-2 sm:m-2 rounded-2xl border border-gray-200 h-full shadow-lg transition-transform hover:scale-[1.03] bg-white"
            >
              <template #header>
                <img
                  :src="`https://castrobrinquedos.onrender.com/static/${item.image}`"
                  :alt="item.type"
                  class="sm:w-full h-52 sm:h-64 object-cover rounded-t-2xl"
                />
              </template>

              <template #title>
                <h3
                  class="text-base sm:text-lg font-bold text-center text-gray-800 mt-3"
                >
                  {{ item.type }}
                </h3>
              </template>

              <template #content>
                <p class="text-sm text-gray-600 text-center px-3 mt-2">
                  {{ item.description }}
                </p>
                <div
                  class="text-center mt-3 font-semibold text-lg sm:text-xl text-rose-500"
                >
                  R$ {{ item.price }}/dia
                </div>
              </template>

              <template #footer>
                <div
                  class="flex flex-col sm:flex-row justify-center items-center gap-3 mt-4 mb-4 px-4"
                >
                  <Button
                    :icon="
                      isProductSelected(item) ? 'pi pi-check' : 'pi pi-plus'
                    "
                    @click="toggleItem(item)"
                    :class="[
                      isProductSelected(item)
                        ? 'p-button-success p-button-outlined'
                        : 'p-button-success'
                    ]"
                    class="w-10 h-10 p-0 flex items-center justify-center rounded-full"
                  />

                  <InputText
                    v-model="item.selectedQuantity"
                    type="number"
                    :min="1"
                    :max="item.static_quantity"
                    placeholder="Qtd"
                    class="w-16 sm:w-20 h-9 text-center border border-gray-300 rounded-md"
                    @input="validateQuantity({ data: item })"
                    @blur="validateQuantity({ data: item })"
                  />
                </div>
              </template>
            </Card>
          </div>
        </div>
      </template>
    </DataView>
  </div>
</template>

<script>
export default {
  data() {
    return {
      layout: 'grid',
    };
  },
  methods: {
    isProductSelected(product) {
      // Lógica para verificar se o produto está selecionado
      return this.selectedProducts?.some(p => p.id === product.id);
    },
    toggleItem(product) {
      // Alternar seleção do item
      if (!this.selectedProducts) this.selectedProducts = [];

      const index = this.selectedProducts.findIndex(p => p.id === product.id);
      if (index !== -1) {
        this.selectedProducts.splice(index, 1);
      } else {
        this.selectedProducts.push({ ...product });
      }
    },
    validateQuantity(slotProps) {
      const item = slotProps.data;
      if (item.selectedQuantity < 1) {
        item.selectedQuantity = 1;
      } else if (item.selectedQuantity > item.static_quantity) {
        item.selectedQuantity = item.static_quantity;
      }
    }
  }
};
</script>
