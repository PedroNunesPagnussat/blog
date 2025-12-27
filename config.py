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
        {'name': 'FastAPI', 'icon': 'devicon-fastapi-plain'},
        {'name': 'PostgreSQL', 'icon': 'devicon-postgresql-plain'},
        {'name': 'MongoDB', 'icon': 'devicon-mongodb-plain'},
        {'name': 'OpenSearch', 'icon': 'devicon-opensearch-original'},
        {'name': 'Docker', 'icon': 'devicon-docker-plain'},
        {'name': 'Linux', 'icon': 'devicon-linux-plain'},
    ]

    TECH_STACK_LINE_2 = [
        {'name': 'LangChain', 'icon': 'fas fa-link'},
        {'name': 'Hugging Face', 'icon': 'fas fa-robot'},
        {'name': 'AWS', 'icon': 'devicon-amazonwebservices-plain-wordmark'},
        {'name': 'GCP', 'icon': 'devicon-googlecloud-plain'},
        {'name': 'Git', 'icon': 'devicon-git-plain'},
        {'name': 'Airflow', 'icon': 'devicon-apacheairflow-plain'},
        {'name': 'DynamoDB', 'icon': 'devicon-dynamodb-plain'},
        {'name': 'Scikit-learn', 'icon': 'devicon-scikitlearn-plain'},
    ]

    # Work Experience Summary (for homepage)
    WORK_EXPERIENCE = {
        'current_project': 'Architecting multimodal RAG systems for visual retrieval across healthcare resources at Elsevier, enabling medical professionals to search clinical images and tables alongside text.',
        'highlights': [
            'Built ML-powered pricing optimization generating $1.8M/year in incremental revenue at Telus Digital',
            'Re-engineered embedding pipeline achieving 72x speedup for daily vector database refreshes',
            'Built LLM-powered sentiment analysis pipeline processing 40,000+ companies for investment decisions',
            'Designed OpenSearch indexing schema with custom chunking, improving search relevance for complex medical queries'
        ]
    }

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
                'Built high-performance image retrieval API with S3 and DynamoDB integration with async streaming, achieving sub-1-second response times at scale',
                'Optimized table extraction pipeline, improving retrieval accuracy by 15% while reducing token consumption by 40%'
            ]
        },
        {
            'company': 'Telus Digital',
            'title': 'Data Scientist',
            'location': 'Porto Alegre, Brazil (Hybrid)',
            'period': 'Nov. 2024 – Sep. 2025',
            'highlights': [
                'Built ML-powered pricing optimization system analyzing product and market features to identify optimal price for Telecom Infrastructure, generating $1.8M/year in incremental revenue',
                'Developed automated international roaming analysis system covering 160+ countries (6x expansion from 25), replacing manual expert reviews and generating $440K/year in revenue'
            ]
        },
        {
            'company': 'Teia Labs',
            'title': 'Junior Data Scientist',
            'location': 'Porto Alegre, Brazil (On-site)',
            'period': 'Jan. 2024 – Nov. 2024',
            'highlights': [
                'Re-engineered embedding pipeline with parallelization and batching, achieving 72x speedup and enabling daily vector database refreshes',
                'Built LLM-powered sentiment analysis pipeline processing 40,000+ companies for investment decision support',
                'Deployed email summarization system using LLMs, reducing analyst review time by 4+ hours/week',
                'Created AI agent research tool synthesizing web data in under 40 seconds',
                'Integrated AI agents with RAG architecture across NoSQL and vector databases for unified cross-source retrieval'
            ]
        },
        {
            'company': 'HP',
            'title': 'Research and Development Data Scientist',
            'location': 'Porto Alegre, Brazil (Hybrid)',
            'period': 'Aug. 2021 – Jan. 2024',
            'highlights': [
                'Optimized SQL analytics queries reducing dashboard load times from minutes to under 5 seconds',
                'Migrated 30+ OMEN gaming dashboards to Power BI, standardizing reporting infrastructure',
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

    RESUME_PATH = '/static/resume.pdf'
