<template>
    <div>
        <div id="main" role="main">
            <div id="">
                <div id="maincontent" class="maincontent">
                    <slot></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            groups: {
                type: Array,
                default: function () {
                    return [];
                }
            }
        },

        data() {
            return {
            }
        },

        computed: {
        },

        activated() {
        },

        methods: {
        }
    };
</script>
