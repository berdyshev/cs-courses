import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const pygameZero = defineCollection({
  loader: glob({ pattern: 'pygame-zero/lesson*/**.md', base: '.' }),
  schema: z.object({
    lesson: z.number(),
    type: z.enum(['handout', 'homework']),
    title: z.string(),
  }),
});

const smartTech = defineCollection({
  loader: glob({ pattern: 'smart-tech/urok*.md', base: '.' }),
  schema: z.object({
    lesson: z.number(),
    title: z.string(),
    grade: z.string(),
    duration: z.string(),
    goal: z.string(),
  }),
});

export const collections = { pygameZero, smartTech };
