<template>
    <div class="card flex justify-center">
        <Menu :model="items">
            <template #item="{ item, props }">
                <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
                    <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                        <span :class="item.icon" />
                        <span class="ml-2">{{ item.label }}</span>
                    </a>
                </router-link>
                <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
                    <span :class="item.icon" />
                    <span class="ml-2">{{ item.label }}</span>
                </a>
            </template>
        </Menu>
    </div>
</template>


<script>
export default{
    data(){
        return{
            items: [
                {
                    label: 'Router Link',
                    icon: 'pi pi-palette',
                    route: '/theming/unstyled'
                },
                {
                    label: 'Programmatic',
                    icon: 'pi pi-link',
                    command: () => {
                        this.$router.push('/introduction');
                    }
                },
                {
                    label: 'External',
                    icon: 'pi pi-home',
                    url: 'https://vuejs.org/'
                }
            ]
        }
    },
}

</script>