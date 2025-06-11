// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Agents Locate',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/lurchingdart/agentslocate' }],
			sidebar: [
				{
					label: 'Getting Started',
					items: [
						'start/introduction',
						{ label: 'Quick Start', link: '/start/start' },
						'start/installation',
					]
				},
				{
					label: 'Architecture & Design',
					items: [
						'architecture/overview',
						'architecture/technical-decisions',
						'architecture/architecture',
						'architecture/data-flow',
						'architecture/monorepo-structure',
					]
				},
				{
					label: 'Core Concepts & Theory',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					items: [
						'core/agent-workflows',
						'core/vector-databases',
						'core/hybrid-search',
						'core/chunking-strategy',
						'core/embeddings',
					]
				},
				{
					label: 'API',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					items: [
						'api/design-principles',
						'api/endpoints',
						'api/response-format',
						'api/error-handling',
					]
				},
				{
					label: 'Frontend Implementation',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					items: [
						'frontend/overview',
						'frontend/nextjs-setup',
						'frontend/ai-sdk-ui-integration',
						'frontend/chat-interface',
					]
				},
				{
					label: 'Database Design',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					items: [
						'database/overview',
						'database/collections-design',
						'database/indexing-approach',
						'database/search-strategies',
					]
				},
				{
					label: 'Implementation',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					autogenerate: { directory: 'implementation' },
				},
				{
					label: 'Development Guide',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					autogenerate: { directory: 'development' },
				},
				{
					label: 'Research Documentation',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					autogenerate: { directory: 'research' },
				},
				{
					label: 'Project Management',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					items: [
						'project/timeline',
						'project/meeting-notes',
						'project/decision-log',
						'project/known-issues',
					]
				},
				{
					label: 'Reference',
					collapsed: true,
					badge: { text: 'WIP', variant: 'caution' },
					items: [
						'reference/glossary',
						'reference/resources',
						'reference/appendix',
					]
				}
			],
			customCss: ['./src/styles/global.css'],
		}),
	],
	vite: {
		plugins: [tailwindcss()],
	},
});
