<script setup>
  import MarkdownIt from 'markdown-it'
  import markdownItKatex from '@vscode/markdown-it-katex'
  import 'katex/dist/katex.min.css'

  const props = defineProps({
    content: {
      type: String,
      required: true,
    }
  })

  console.log(props.content)

  const md = new MarkdownIt({
    html: false,
    linkify: true,
    typographer: true
  })
  md.use(markdownItKatex.default || markdownItKatex)

  const contentHTML = computed(() => md.render(props.content))
</script>

<template>
  <div class=post v-html=contentHTML></div>
</template>
