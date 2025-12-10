from django.shortcuts import render

# Home/Projects Page
def home_view(request):
    context = {
        'active_page': 'projects',
        'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'Git'],
        'languages': ['Python', 'JavaScript', 'SQL'],
        'projects': [
            {
                'id': 1,
                'title': 'Portfolio Website',
                'description': 'Monochrome Django portfolio with responsive design',
                'tech': ['HTML', 'CSS', 'Python', 'Django']
            },
            {
                'id': 2,
                'title': 'E-Commerce Platform',
                'description': 'Full-featured online store with cart and payment',
                'tech': ['Python', 'Django', 'JavaScript', 'SQLite']
            },
            {
                'id': 3,
                'title': 'Task Management App',
                'description': 'Productivity app for managing daily tasks',
                'tech': ['JavaScript', 'React', 'Node.js']
            },
        ]
    }
    return render(request, 'myapp/index.html', context)

# About Me Page
def about_view(request):
    context = {
        'active_page': 'about',
        'bio': "Hello! I'm Jerome, a Product Manager & Maker based in London. Ever since I began learning programming and working on small projects, I discovered how much I enjoy turning ideas into tangible solutions.",
        'education': "Bachelor of Information Technology",
        'skills': {
            'Technical': ['HTML/CSS', 'JavaScript', 'Python', 'Django', 'Git', 'SQL'],
            'Soft Skills': ['Problem Solving', 'Communication', 'Teamwork', 'Project Management'],
        },
        'languages': ['English (Fluent)', 'Spanish (Intermediate)'],
        'interests': ['Web Development', 'UI/UX Design', 'Product Strategy', 'Open Source']
    }
    return render(request, 'myapp/about.html', context)

# Writing/Blog Page
def writing_view(request):
    context = {
        'active_page': 'writing',
        'articles': [
            {
                'title': 'Getting Started with Django',
                'date': 'Dec 5, 2024',
                'excerpt': 'A beginner-friendly guide to building web applications with Django',
                'read_time': '5 min read'
            },
            {
                'title': 'The Importance of Clean Code',
                'date': 'Nov 28, 2024',
                'excerpt': 'Why writing maintainable code matters for long-term project success',
                'read_time': '8 min read'
            },
            {
                'title': 'Monochrome Design Principles',
                'date': 'Nov 15, 2024',
                'excerpt': 'Exploring minimalist design and its impact on user experience',
                'read_time': '6 min read'
            },
        ]
    }
    return render(request, 'myapp/writing.html', context)

# Contact Page
def contact_view(request):
    context = {
        'active_page': 'contact',
        'email': 'jerome@example.com',
        'linkedin': 'https://linkedin.com/in/jerome',
        'github': 'https://github.com/jerome',
    }
    return render(request, 'myapp/contact.html', context)
