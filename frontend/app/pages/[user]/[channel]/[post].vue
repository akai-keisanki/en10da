<script setup>
  import MarkdownIt from 'markdown-it'
  import markdownItKatex from '@vscode/markdown-it-katex'
  import 'katex/dist/katex.min.css'

  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel
  const post = route.params.post

  const {get} = useAPI()

  const resp = await get(`post/${user}/${channel}/${post}`)
  const title = resp.data.title;
  // const content = resp.data.content;
  const content = `
This is a test of
- maybe \\LaTeX: $2^{-1}at^2 + v_0t + s_0 = s$
- maybe **mark***down*
  `;

  const md = new MarkdownIt({
    html: false,
    linkify: true,
    typographer: true
  })
  md.use(markdownItKatex.default || markdownItKatex)

  const contentHTML = computed(() => md.render(content))
</script>

<template>
  <page :title=title :subtitle='`${user}/${channel}/${post}`'>
    <div v-html=contentHTML></div>
  </page>
</template>
