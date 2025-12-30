import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CONTENT_DIR = os.path.join(BASE_DIR, 'content')
    POSTS_DIR = os.path.join(CONTENT_DIR, 'posts')
    PROJECTS_DIR = os.path.join(CONTENT_DIR, 'projects')

    # Personal Information
    PROFILE = {
        'name': 'Pedro Nunes Pagnussat',
        'title': 'Senior AI Engineer',
        'bio': 'AI/ML Engineer with 5+ years building production systems in healthcare, telecom, and finance. Expertise in LLMs, RAG, and ML pipelines. Delivered $2.2M+ annual revenue and 72x performance gains.',
        'email': 'np.pedro.np@gmail.com',
        'linkedin': 'https://linkedin.com/in/pedronp',
        'github': 'https://github.com/PedroNunesPagnussat',
        'profile_image': '/static/images/profile.jpg'
    }

    # Tech Stack Carousel - Two lines moving in opposite directions
    # Uses Devicon class names: https://devicon.dev/
    TECH_STACK_LINE_1 = [
        {'name': 'Python', 'icon': 'devicon-python-plain'},
        {'name': 'PyTorch', 'icon': 'devicon-pytorch-original'},
        {'name': 'OpenAI', 'svg': '/static/images/logos/openai-svgrepo-com.svg'},
        {'name': 'Hugging Face', 'svg': '/static/images/logos/huggingface.svg'},
        {'name': 'LangGraph', 'svg': '/static/images/logos/langgraph.svg'},
        {'name': 'FastAPI', 'icon': 'devicon-fastapi-plain'},
        {'name': 'AWS', 'icon': 'devicon-amazonwebservices-plain-wordmark'},
        {'name': 'GCP', 'icon': 'devicon-googlecloud-plain'},
    ]
    TECH_STACK_LINE_2 = [
        {'name': 'PostgreSQL', 'icon': 'devicon-postgresql-plain'},
        {'name': 'MongoDB', 'icon': 'devicon-mongodb-plain'},
        {'name': 'DynamoDB', 'icon': 'devicon-dynamodb-plain'},
        {'name': 'Docker', 'icon': 'devicon-docker-plain'},
        {'name': 'Airflow', 'icon': 'devicon-apacheairflow-plain'},
        {'name': 'Git', 'icon': 'devicon-git-plain'},
        # Repeting
        {'name': 'PostgreSQL', 'icon': 'devicon-postgresql-plain'},
        {'name': 'MongoDB', 'icon': 'devicon-mongodb-plain'},
        {'name': 'DynamoDB', 'icon': 'devicon-dynamodb-plain'},
        {'name': 'Docker', 'icon': 'devicon-docker-plain'},
        {'name': 'Airflow', 'icon': 'devicon-apacheairflow-plain'},
        {'name': 'Git', 'icon': 'devicon-git-plain'},
        # {'name': 'Pinecone', 'icon': 'devicon-pinecone-plain'}
    ]


    # Full Experience Timeline
    EXPERIENCE = [
        {
            'company': 'Elsevier',
            'title': 'Senior AI Engineer',
            'location': 'Remote',
            'period': 'Sep. 2025 – Present',
            'highlights': [
                'Architected multimodal RAG system for visual retrieval across healthcare resources, enabling medical professionals to search clinical images and tables alongside text',
                'Designed OpenSearch indexing schema with custom chunking and metadata enrichment, improving search relevance for complex medical queries',
                'Built high-performance image retrieval API with S3 and DynamoDB integration with async streaming, achieving <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">sub-1-second response times</strong> at scale',
                'Optimized table extraction pipeline, improving retrieval accuracy by <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">15%</strong> while reducing token consumption by <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">40%</strong>'
            ]
        },
        {
            'company': 'Telus Digital',
            'title': 'Data Scientist',
            'location': 'Porto Alegre, Brazil (Hybrid)',
            'period': 'Nov. 2024 – Sep. 2025',
            'highlights': [
                'Built ML-powered pricing optimization system analyzing product and market features to identify optimal price for Telecom Infrastructure, generating <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">$1.8M/year</strong> in incremental revenue',
                'Developed automated international roaming analysis system covering <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">160+ countries</strong> (6x expansion from 25), replacing manual expert reviews and generating <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">$440K/year</strong> in revenue'
            ]
        },
        {
            'company': 'Teia Labs',
            'title': 'Junior Data Scientist',
            'location': 'Porto Alegre, Brazil (On-site)',
            'period': 'Jan. 2024 – Nov. 2024',
            'highlights': [
                'Re-engineered embedding pipeline with parallelization and batching, achieving <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">72x speedup</strong> and enabling daily vector database refreshes',
                'Built LLM-powered sentiment analysis pipeline processing <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">40,000+ companies</strong> for investment decision support',
                'Deployed email summarization system using LLMs, reducing analyst review time by <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">4+ hours/week</strong>',
                'Created AI agent research tool synthesizing web data in <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">under 40 seconds</strong>',
                'Integrated AI agents with RAG architecture across NoSQL and vector databases for unified cross-source retrieval'
            ]
        },
        {
            'company': 'HP',
            'title': 'Research and Development Data Scientist',
            'location': 'Porto Alegre, Brazil (Hybrid)',
            'period': 'Aug. 2021 – Jan. 2024',
            'highlights': [
                'Optimized SQL analytics queries reducing dashboard load times from minutes to <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">under 5 seconds</strong>',
                'Migrated <strong class="text-ctpl-mauve dark:text-ctp-mauve font-semibold">30+ OMEN gaming dashboards</strong> to Power BI, standardizing reporting infrastructure',
                'Built R&D for document intelligence: classification, NER-based auto-renaming, and semantic segmentation for document processing'
            ]
        }
    ]

    # Education
    EDUCATION = [
        {
            'degree': 'MBA in Project Management and Agile Methodologies',
            'institution': 'Pontifical Catholic University of Rio Grande do Sul (PUC-RS)',
            'location': 'Porto Alegre, Brazil',
            'period': 'Dec. 2025 – Dec. 2026'
        },
        {
            'degree': 'Bachelor of Science in Data Science and Artificial Intelligence',
            'institution': 'Pontifical Catholic University of Rio Grande do Sul (PUC-RS)',
            'location': 'Porto Alegre, Brazil',
            'period': 'Mar. 2020 – Dec. 2024'
        }
    ]

    # Languages
    LANGUAGES = [
        {'name': 'Portuguese', 'level': 'Native'},
        {'name': 'English', 'level': 'C1'},
        {'name': 'Spanish', 'level': 'Conversational'},
        {'name': 'Chinese', 'level': 'HSK1'}
    ]

    RESUME_PATH = '/static/resume.pdf'

    # Custom domain for GitHub Pages (set to None to use default github.io domain)
    DOMAIN = None
