<template>
    <kw-layout>
        <div class="header">
            <span>CCTV1</span>
        </div>
        <div class="list">
            <dl v-for="item in apiData" :key="item.id">
                <router-link :to="{path: '/detail', query: {id: item.id, tv: 'cctv1'}}">
                    <dt>
                        <img style="width: 100%; height: 100%" :src="item.image">
                    </dt>
                    <dd>
                        <a>{{ item.name }}</a>
                        <p>{{ item.des }}</p>
                    </dd>
                </router-link>
            </dl>
        </div>
    </kw-layout>
</template>

<script>
    export default {
        data() {
            return {
                url: this.api + '/weshow/',
                apiData: []
            };
        },

        mounted() {
        },

        activated() {
            this.search();
        },

        methods: {
            search() {
                this.$http.get(this.url + '?tv=cctv1').then((response) => {
                    this.apiData = response.data.results;
                });
            }
        }
    }
</script>

<style>
</style>
