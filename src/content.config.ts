import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const lessons = defineCollection({
  loader: glob({ pattern: 'lesson*/**.md', base: '.' }),
  schema: z.object({
    lesson: z.number(),
    type: z.enum(['handout', 'homework']),
    title: z.string(),
  }),
});

export const collections = { lessons };
