import { defineStore } from 'pinia'

export const useAmountStore = defineStore('amountStore', {
  state: () => ({
    amount: 0.0,
    storeProducts: [],
    disableDates: [],
    disabledDates: [],
  }),

})
