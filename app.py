from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Portfolio | ICT & Cybersecurity</title>
        
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html {
                scroll-behavior: smooth;
            }

            body {
                font-family: Arial, sans-serif;
                background: #0b1020;
                color: white;
                line-height: 1.6;
            }

            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px 8%;
                background: #11182b;
                position: sticky;
                top: 0;
                z-index: 10;
                flex-wrap: wrap;
                gap: 15px;
            }

            .logo {
                font-size: 24px;
                font-weight: bold;
                color: #00e5ff;
            }

            nav a {
                color: white;
                text-decoration: none;
                margin-left: 18px;
                font-size: 14px;
            }

            nav a:hover {
                color: #00e5ff;
            }

            .hero {
                min-height: 85vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 60px 20px;
                background:
                    radial-gradient(circle at top right, #173c65, transparent 45%),
                    linear-gradient(135deg, #0b1020, #15102d);
            }

            .tag {
                color: #00e5ff;
                border: 1px solid #00e5ff;
                padding: 8px 18px;
                border-radius: 30px;
                margin-bottom: 24px;
            }

            .hero h1 {
                font-size: clamp(38px, 7vw, 68px);
                line-height: 1.15;
                margin-bottom: 20px;
            }

            .hero h1 span {
                color: #00e5ff;
            }

            .hero p {
                max-width: 650px;
                color: #c0c8db;
                font-size: 18px;
                margin-bottom: 30px;
            }

            .btn {
                display: inline-block;
                background: #00d5e8;
                color: #07111f;
                padding: 13px 25px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                margin: 5px;
                transition: 0.3s;
            }

            .btn:hover {
                background: white;
                transform: translateY(-3px);
            }

            .btn-outline {
                border: 1px solid #00e5ff;
                color: #00e5ff;
                background: transparent;
            }

            section {
                padding: 80px 8%;
                scroll-margin-top: 75px;
            }

            .section-title {
                text-align: center;
                font-size: 34px;
                margin-bottom: 15px;
            }

            .section-intro {
                color: #aab6ce;
                text-align: center;
                max-width: 650px;
                margin: 0 auto 40px;
            }

            .about {
                max-width: 800px;
                margin: auto;
                text-align: center;
                color: #c0c8db;
                font-size: 17px;
            }

            .skills, .projects {
                display: grid;
                grid-template-columns:
                    repeat(auto-fit, minmax(220px, 1fr));
                gap: 22px;
            }

            .card {
                background: #141d33;
                border: 1px solid #263650;
                padding: 28px;
                border-radius: 16px;
                transition: 0.3s;
            }

            .card:hover {
                transform: translateY(-7px);
                border-color: #00e5ff;
            }

            .card .emoji {
                font-size: 35px;
                margin-bottom: 15px;
            }

            .card h3 {
                color: #00e5ff;
                margin-bottom: 12px;
            }

            .card p {
                color: #bdc7d9;
            }

            .contact {
                text-align: center;
                background: #11182b;
            }

            .contact p {
                color: #bdc7d9;
                margin: 15px auto 25px;
            }

            footer {
                text-align: center;
                padding: 25px;
                color: #8996af;
                border-top: 1px solid #263650;
            }

            @media (max-width: 600px) {
                nav {
                    justify-content: center;
                }

                nav a {
                    margin: 0 7px;
                }

                section {
                    padding: 60px 6%;
                }

                .hero {
                    min-height: 75vh;
                }
            }
        .profile-photo {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 50%;
    border: 4px solid #00e5ff;
    margin-bottom: 25px;
    box-shadow: 0 0 25px #00e5ff55;
}
        </style>
    </head>

    <body>

        <nav>
            <div class="logo">&lt;MyPortfolio /&gt;</div>
            <div>
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
          <a href="/static/Dennis_Kimiri_CV,pdf..pdf" class="btn" download>Download My CV</a> 
             </div>
        </nav>

        <header class="hero" id="home">
            <div class="tag">ICT TECHNICIAN | FUTURE CYBERSECURITY PROFESSIONAL</div>

      <img src="/static/profile.jpg"
     alt="Dennis's profile photo"
     class="profile-photo">
                  <h1>Hello, I'm <span>Dennis Kimiri</span></h1>

            <p>
                Welcome to my digital space. I'm learning technology,
                Python, networking, and cybersecurity, one project
                at a time.
            </p>

            <div>
                <a href="#projects" class="btn">Explore My Work</a>
                <a href="#contact" class="btn btn-outline">Contact Me</a>
            </div>
        </header>

        <section id="about">
            <h2 class="section-title">About Me</h2>
            <p class="section-intro">A little about my journey in technology</p>

            <div class="about">
                <p>
                    I'm an aspiring ICT professional passionate about
                    computers, technology, and solving technical problems.
                    I'm building my skills in computer maintenance,
                    networking, Python programming, and cybersecurity.
                    My goal is to keep learning and develop solutions
                    that make a difference.
                </p>
            </div>
        </section>

        <section id="skills">
            <h2 class="section-title">My Skills</h2>
            <p class="section-intro">
                Technologies and areas I'm learning and practising
            </p>

            <div class="skills">
                <div class="card">
                    <div class="emoji">🖥️</div>
                    <h3>Computer Maintenance</h3>
                    <p>Computer setup, troubleshooting, software installation, and maintenance.</p>
                </div>

                <div class="card">
                    <div class="emoji">🌐</div>
                    <h3>Networking</h3>
                    <p>IP addressing, Ethernet cables, network configuration, and troubleshooting.</p>
                </div>

                <div class="card">
                    <div class="emoji">🐍</div>
                    <h3>Python Programming</h3>
                    <p>Learning Python fundamentals and building useful applications.</p>
                </div>

                <div class="card">
                    <div class="emoji">🔐</div>
                    <h3>Cybersecurity</h3>
                    <p>Developing knowledge of Linux, security fundamentals, and safe security labs.</p>
                </div>
            </div>
        </section>

        <section id="projects">
            <h2 class="section-title">My Projects</h2>
            <p class="section-intro">
                A growing collection of my practical work
            </p>

            <div class="projects">
                <div class="card">
                    <div class="emoji">💻</div>
                    <h3>Personal Portfolio</h3>
                    <p>A portfolio website built using Python, Flask, HTML, and CSS.</p>
                 <a href="https://github.com/" target="_blank" class="btn">View Code</a>   
                </div>

                <div class="card">
                    <div class="emoji">🛠️</div>
                    <h3>ICT Practice</h3>
                    <p>Practical exercises in computer troubleshooting and networking.</p>
                </div>

                <div class="card">
                    <div class="emoji">🛡️</div>
                    <h3>Cybersecurity Labs</h3>
                    <p>My learning journey through authorised security exercises and labs.</p>
                </div>
            </div>
        </section>

        <section id="contact" class="contact">
            <h2 class="section-title">Let's Connect</h2>
            <p>
                Interested in technology or collaborating on a project?
                I'd be happy to connect.
            </p>
            <a href="mailto:your-denniskimiri7@gmail.com" class="btn">
                Email Me
            </a>
        </section>

        <footer>
            <p>&copy; 2026 My Portfolio. Built with Python and Flask.</p>
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)