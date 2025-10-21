import streamlit as st
import pandas as pd
import plotly.express as px

# Sample resume data with the new structure
initial_resumes = [
   
   
  {
    "name": "Avni Verma",
    "email": "avni.verma@yahoo.com",
    "phone": "330-677-8039",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Angular"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sai Iyer",
    "email": "sai.iyer@gmail.com",
    "phone": "691-993-3080",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "NexGen",
    "skills": [
      "Java"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Vihaan Das",
    "email": "vihaan.das@outlook.com",
    "phone": "437-853-6864",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Ruby"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@outlook.com",
    "phone": "944-760-5324",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "JavaScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Priya Chopra",
    "email": "priya.chopra@example.com",
    "phone": "537-922-9429",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "TechCorp",
    "skills": [
      "DevOps"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarya Joshi",
    "email": "aarya.joshi@outlook.com",
    "phone": "804-458-3139",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Java"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Saanvi Chowdhury",
    "email": "saanvi.chowdhury@gmail.com",
    "phone": "416-354-9591",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "FutureTech",
    "skills": [
      "Node.js"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Saanvi Iyer",
    "email": "saanvi.iyer@gmail.com",
    "phone": "817-691-5921",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "HTML"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Saanvi Chopra",
    "email": "saanvi.chopra@yahoo.com",
    "phone": "946-741-9034",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "Vue"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Priya Sharma",
    "email": "priya.sharma@yahoo.com",
    "phone": "148-224-1532",
    "ATS_score": 1,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Agile"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Vivaan Verma",
    "email": "vivaan.verma@gmail.com",
    "phone": "325-531-1314",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Digital Solutions",
    "skills": [
      "React"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ayaan Chopra",
    "email": "ayaan.chopra@yahoo.com",
    "phone": "343-225-4593",
    "ATS_score": 2,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Creative Minds",
    "skills": [
      "Data Science"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Diya Nair",
    "email": "diya.nair@outlook.com",
    "phone": "891-576-9207",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "InnovateX",
    "skills": [
      "GraphQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vihaan Chowdhury",
    "email": "vihaan.chowdhury@yahoo.com",
    "phone": "151-823-5425",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Rust"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Reyansh Roy",
    "email": "reyansh.roy@example.com",
    "phone": "735-839-3663",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "NexGen",
    "skills": [
      "Java"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Kavya Kapoor",
    "email": "kavya.kapoor@yahoo.com",
    "phone": "333-981-7663",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Git"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarya Kapoor",
    "email": "aarya.kapoor@yahoo.com",
    "phone": "319-300-5479",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "NexGen",
    "skills": [
      "DevOps"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Avni Roy",
    "email": "avni.roy@example.com",
    "phone": "293-686-4430",
    "ATS_score": 2,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "JavaScript"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ananya Pillai",
    "email": "ananya.pillai@outlook.com",
    "phone": "638-679-2654",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Django"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Arjun Patel",
    "email": "arjun.patel@example.com",
    "phone": "921-239-1005",
    "ATS_score": 2,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "Spring"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aditya Chopra",
    "email": "aditya.chopra@example.com",
    "phone": "308-467-7280",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarya Iyer",
    "email": "aarya.iyer@gmail.com",
    "phone": "740-556-2800",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Ruby"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Kavya Bhat",
    "email": "kavya.bhat@example.com",
    "phone": "742-701-9510",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "CSS"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Vivaan Reddy",
    "email": "vivaan.reddy@gmail.com",
    "phone": "776-397-8754",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "DataWorks",
    "skills": [
      "Go"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Priya Jain",
    "email": "priya.jain@outlook.com",
    "phone": "827-344-5406",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Spring"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Sai Mehta",
    "email": "sai.mehta@outlook.com",
    "phone": "290-903-6258",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Rust"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Das",
    "email": "avni.das@example.com",
    "phone": "435-466-1039",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Django"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Saanvi Menon",
    "email": "saanvi.menon@example.com",
    "phone": "276-342-5760",
    "ATS_score": 3,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "Java"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ayaan Verma",
    "email": "ayaan.verma@gmail.com",
    "phone": "732-302-7005",
    "ATS_score": 3,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Vue"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Diya Sharma",
    "email": "diya.sharma@yahoo.com",
    "phone": "588-617-8816",
    "ATS_score": 3,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Vue"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Vihaan Roy",
    "email": "vihaan.roy@yahoo.com",
    "phone": "661-338-5347",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Data Insights",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Reyansh Chowdhury",
    "email": "reyansh.chowdhury@outlook.com",
    "phone": "114-508-3671",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "DevOps"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Kavya Singh",
    "email": "kavya.singh@yahoo.com",
    "phone": "622-263-9575",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Spring"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ishaan Bhat",
    "email": "ishaan.bhat@gmail.com",
    "phone": "115-885-5268",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "NexGen",
    "skills": [
      "DevOps"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Myra Jain",
    "email": "myra.jain@example.com",
    "phone": "508-590-1243",
    "ATS_score": 4,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Angular"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Sai Kapoor",
    "email": "sai.kapoor@example.com",
    "phone": "407-703-5659",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "NoSQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ayaan Menon",
    "email": "ayaan.menon@yahoo.com",
    "phone": "872-478-7879",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Flask"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ira Verma",
    "email": "ira.verma@outlook.com",
    "phone": "171-201-4301",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "CSS"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Mehta",
    "email": "avni.mehta@yahoo.com",
    "phone": "416-492-9773",
    "ATS_score": 4,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "JavaScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Vihaan Jain",
    "email": "vihaan.jain@outlook.com",
    "phone": "714-976-6879",
    "ATS_score": 4,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Rust"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Reyansh Gupta",
    "email": "reyansh.gupta@yahoo.com",
    "phone": "193-752-3986",
    "ATS_score": 5,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "TechWave",
    "skills": [
      "Azure"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Myra Kumar",
    "email": "myra.kumar@outlook.com",
    "phone": "138-681-3380",
    "ATS_score": 5,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "JavaScript"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Kavya Iyer",
    "email": "kavya.iyer@yahoo.com",
    "phone": "684-205-3719",
    "ATS_score": 5,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "GraphQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Vivaan Nair",
    "email": "vivaan.nair@outlook.com",
    "phone": "288-864-8721",
    "ATS_score": 5,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Go"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Vihaan Pillai",
    "email": "vihaan.pillai@example.com",
    "phone": "865-556-3110",
    "ATS_score": 5,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Go"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Aarya Kumar",
    "email": "aarya.kumar@example.com",
    "phone": "731-923-3010",
    "ATS_score": 5,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Scrum"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Diya Reddy",
    "email": "diya.reddy@gmail.com",
    "phone": "232-281-4876",
    "ATS_score": 5,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "DevOps"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Vivaan Iyer",
    "email": "vivaan.iyer@yahoo.com",
    "phone": "351-452-5178",
    "ATS_score": 5,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "AWS"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Vihaan Iyer",
    "email": "vihaan.iyer@yahoo.com",
    "phone": "917-344-9453",
    "ATS_score": 5,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Scrum"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Saanvi Chowdhury",
    "email": "saanvi.chowdhury@gmail.com",
    "phone": "701-312-2140",
    "ATS_score": 5,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Data Science"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Priya Patel",
    "email": "priya.patel@example.com",
    "phone": "480-142-2296",
    "ATS_score": 6,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "Flask"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aditya Iyer",
    "email": "aditya.iyer@outlook.com",
    "phone": "421-708-1584",
    "ATS_score": 6,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "GraphQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Saanvi Das",
    "email": "saanvi.das@yahoo.com",
    "phone": "655-579-6775",
    "ATS_score": 6,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Rust"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Sara Mehta",
    "email": "sara.mehta@outlook.com",
    "phone": "787-272-3365",
    "ATS_score": 6,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "CSS"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Avni Joshi",
    "email": "avni.joshi@gmail.com",
    "phone": "832-531-9521",
    "ATS_score": 6,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Flask"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aditya Jain",
    "email": "aditya.jain@yahoo.com",
    "phone": "629-608-8507",
    "ATS_score": 6,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "InnovateX",
    "skills": [
      "Ruby"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aditya Gupta",
    "email": "aditya.gupta@yahoo.com",
    "phone": "540-314-2332",
    "ATS_score": 6,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Scrum"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ananya Nair",
    "email": "ananya.nair@outlook.com",
    "phone": "978-228-8935",
    "ATS_score": 6,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Git"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ishaan Kumar",
    "email": "ishaan.kumar@gmail.com",
    "phone": "160-994-6129",
    "ATS_score": 6,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Ruby"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarya Patel",
    "email": "aarya.patel@yahoo.com",
    "phone": "493-951-4333",
    "ATS_score": 6,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "DataWorks",
    "skills": [
      "Agile"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Arjun Bhat",
    "email": "arjun.bhat@outlook.com",
    "phone": "782-102-6009",
    "ATS_score": 7,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "TechWave",
    "skills": [
      "AWS"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ishaan Patel",
    "email": "ishaan.patel@outlook.com",
    "phone": "578-246-6279",
    "ATS_score": 7,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ishaan Jain",
    "email": "ishaan.jain@example.com",
    "phone": "281-218-7358",
    "ATS_score": 7,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "HTML"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ishaan Jain",
    "email": "ishaan.jain@outlook.com",
    "phone": "416-790-5029",
    "ATS_score": 7,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "Vue"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vivaan Nair",
    "email": "vivaan.nair@gmail.com",
    "phone": "587-139-1650",
    "ATS_score": 7,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "JavaScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Diya Mehta",
    "email": "diya.mehta@yahoo.com",
    "phone": "938-496-2023",
    "ATS_score": 7,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "React"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ayaan Chopra",
    "email": "ayaan.chopra@outlook.com",
    "phone": "903-365-2981",
    "ATS_score": 7,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Global Solutions",
    "skills": [
      "Docker"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarav Mehta",
    "email": "aarav.mehta@outlook.com",
    "phone": "604-884-9111",
    "ATS_score": 7,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "HTML"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ananya Sharma",
    "email": "ananya.sharma@example.com",
    "phone": "225-458-3717",
    "ATS_score": 7,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "Ruby"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Vivaan Gupta",
    "email": "vivaan.gupta@gmail.com",
    "phone": "584-311-8332",
    "ATS_score": 7,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Go"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Aarya Mehta",
    "email": "aarya.mehta@gmail.com",
    "phone": "441-957-6247",
    "ATS_score": 8,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "Docker"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Vivaan Sharma",
    "email": "vivaan.sharma@yahoo.com",
    "phone": "255-721-6159",
    "ATS_score": 8,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "NoSQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ishaan Joshi",
    "email": "ishaan.joshi@yahoo.com",
    "phone": "167-766-6106",
    "ATS_score": 8,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "JavaScript"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Vihaan Roy",
    "email": "vihaan.roy@gmail.com",
    "phone": "595-983-5964",
    "ATS_score": 8,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "SQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarya Mehta",
    "email": "aarya.mehta@outlook.com",
    "phone": "992-766-7694",
    "ATS_score": 8,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Ruby"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Diya Kumar",
    "email": "diya.kumar@yahoo.com",
    "phone": "444-746-7193",
    "ATS_score": 8,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Data Insights",
    "skills": [
      "Node.js"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Reyansh Pillai",
    "email": "reyansh.pillai@outlook.com",
    "phone": "425-894-2593",
    "ATS_score": 8,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Data Insights",
    "skills": [
      "TypeScript"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Krishna Singh",
    "email": "krishna.singh@gmail.com",
    "phone": "176-468-6398",
    "ATS_score": 8,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "C#"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Sai Pillai",
    "email": "sai.pillai@example.com",
    "phone": "551-419-4964",
    "ATS_score": 8,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechWave",
    "skills": [
      "CSS"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Saanvi Reddy",
    "email": "saanvi.reddy@example.com",
    "phone": "711-525-6409",
    "ATS_score": 8,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Data Science"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Kavya Iyer",
    "email": "kavya.iyer@example.com",
    "phone": "444-865-7051",
    "ATS_score": 9,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "TypeScript"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ananya Chopra",
    "email": "ananya.chopra@gmail.com",
    "phone": "940-323-3051",
    "ATS_score": 9,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Data Science"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Saanvi Singh",
    "email": "saanvi.singh@outlook.com",
    "phone": "397-870-3735",
    "ATS_score": 9,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Spring"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ira Chopra",
    "email": "ira.chopra@yahoo.com",
    "phone": "753-302-6220",
    "ATS_score": 9,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Java"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Reyansh Das",
    "email": "reyansh.das@outlook.com",
    "phone": "666-763-3409",
    "ATS_score": 9,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Rust"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Arjun Pillai",
    "email": "arjun.pillai@yahoo.com",
    "phone": "160-170-8421",
    "ATS_score": 9,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Data Science"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ananya Nair",
    "email": "ananya.nair@example.com",
    "phone": "839-943-5984",
    "ATS_score": 9,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Node.js"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Reyansh Patel",
    "email": "reyansh.patel@example.com",
    "phone": "491-903-9098",
    "ATS_score": 9,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Node.js"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ayaan Nair",
    "email": "ayaan.nair@gmail.com",
    "phone": "148-853-3271",
    "ATS_score": 9,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "JavaScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarya Sharma",
    "email": "aarya.sharma@outlook.com",
    "phone": "241-575-8299",
    "ATS_score": 9,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Node.js"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ira Jain",
    "email": "ira.jain@outlook.com",
    "phone": "834-691-9471",
    "ATS_score": 10,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Spring"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Diya Joshi",
    "email": "diya.joshi@example.com",
    "phone": "472-546-9905",
    "ATS_score": 10,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "Java"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Krishna Reddy",
    "email": "krishna.reddy@outlook.com",
    "phone": "482-876-2158",
    "ATS_score": 10,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Django"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aarav Kumar",
    "email": "aarav.kumar@example.com",
    "phone": "274-749-4881",
    "ATS_score": 10,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Data Insights",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Arjun Reddy",
    "email": "arjun.reddy@example.com",
    "phone": "128-245-8670",
    "ATS_score": 10,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Java"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Pillai",
    "email": "sara.pillai@yahoo.com",
    "phone": "452-578-2802",
    "ATS_score": 10,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Docker"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Saanvi Kapoor",
    "email": "saanvi.kapoor@gmail.com",
    "phone": "214-270-4774",
    "ATS_score": 10,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "FutureTech",
    "skills": [
      "Ruby"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Diya Kapoor",
    "email": "diya.kapoor@example.com",
    "phone": "493-793-5220",
    "ATS_score": 10,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DevSolutions",
    "skills": [
      "Azure"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Avni Verma",
    "email": "avni.verma@outlook.com",
    "phone": "524-616-9424",
    "ATS_score": 10,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Node.js"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Avni Chowdhury",
    "email": "avni.chowdhury@example.com",
    "phone": "270-969-3769",
    "ATS_score": 10,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Ruby"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Intern"
  },
  {
    "name": "Kavya Bhat",
    "email": "kavya.bhat@gmail.com",
    "phone": "647-583-2615",
    "ATS_score": 11,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "React"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Diya Pillai",
    "email": "diya.pillai@example.com",
    "phone": "800-665-3507",
    "ATS_score": 11,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Vue"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Avni Kapoor",
    "email": "avni.kapoor@yahoo.com",
    "phone": "359-196-7731",
    "ATS_score": 11,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "Django"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ayaan Sharma",
    "email": "ayaan.sharma@example.com",
    "phone": "917-840-4934",
    "ATS_score": 11,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "NexGen",
    "skills": [
      "Rust"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Sai Menon",
    "email": "sai.menon@yahoo.com",
    "phone": "720-151-9282",
    "ATS_score": 11,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "TechWave",
    "skills": [
      "Go"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ishaan Singh",
    "email": "ishaan.singh@example.com",
    "phone": "232-163-7323",
    "ATS_score": 11,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "HTML"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Gupta",
    "email": "ayaan.gupta@example.com",
    "phone": "166-836-4583",
    "ATS_score": 11,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Global Solutions",
    "skills": [
      "NoSQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Aarav Gupta",
    "email": "aarav.gupta@yahoo.com",
    "phone": "538-118-1878",
    "ATS_score": 11,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "Rust"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Priya Kapoor",
    "email": "priya.kapoor@outlook.com",
    "phone": "572-777-3305",
    "ATS_score": 11,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Django"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ayaan Verma",
    "email": "ayaan.verma@example.com",
    "phone": "169-349-4475",
    "ATS_score": 11,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Docker"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Arjun Nair",
    "email": "arjun.nair@yahoo.com",
    "phone": "912-560-8180",
    "ATS_score": 12,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Spring"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarya Das",
    "email": "aarya.das@example.com",
    "phone": "274-661-5771",
    "ATS_score": 12,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sai Das",
    "email": "sai.das@outlook.com",
    "phone": "276-944-2171",
    "ATS_score": 12,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "Scrum"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Myra Roy",
    "email": "myra.roy@yahoo.com",
    "phone": "413-728-1689",
    "ATS_score": 12,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "Spring"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Saanvi Chopra",
    "email": "saanvi.chopra@yahoo.com",
    "phone": "283-185-3609",
    "ATS_score": 12,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Spring"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Sara Gupta",
    "email": "sara.gupta@gmail.com",
    "phone": "727-849-5931",
    "ATS_score": 12,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Spring"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Myra Menon",
    "email": "myra.menon@outlook.com",
    "phone": "659-149-1897",
    "ATS_score": 12,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Vue"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Jain",
    "email": "krishna.jain@gmail.com",
    "phone": "352-971-6304",
    "ATS_score": 12,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Avni Sharma",
    "email": "avni.sharma@example.com",
    "phone": "567-915-2658",
    "ATS_score": 12,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NexGen",
    "skills": [
      "Azure"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Saanvi Chopra",
    "email": "saanvi.chopra@example.com",
    "phone": "367-937-3138",
    "ATS_score": 12,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "TechCorp",
    "skills": [
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Saanvi Joshi",
    "email": "saanvi.joshi@outlook.com",
    "phone": "356-352-7245",
    "ATS_score": 13,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "TypeScript"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aarav Kumar",
    "email": "aarav.kumar@gmail.com",
    "phone": "700-412-6720",
    "ATS_score": 13,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "TechWave",
    "skills": [
      "C#"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Priya Patel",
    "email": "priya.patel@yahoo.com",
    "phone": "292-800-3084",
    "ATS_score": 13,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sara Sharma",
    "email": "sara.sharma@outlook.com",
    "phone": "721-548-1821",
    "ATS_score": 13,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "DevOps"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Arjun Kumar",
    "email": "arjun.kumar@gmail.com",
    "phone": "377-770-3613",
    "ATS_score": 13,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "AWS"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ira Gupta",
    "email": "ira.gupta@outlook.com",
    "phone": "129-604-7222",
    "ATS_score": 13,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Creative Minds",
    "skills": [
      "Agile"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Reyansh Mehta",
    "email": "reyansh.mehta@example.com",
    "phone": "550-328-8858",
    "ATS_score": 13,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "FutureTech",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ira Nair",
    "email": "ira.nair@example.com",
    "phone": "579-733-8772",
    "ATS_score": 13,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Node.js"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Kavya Chowdhury",
    "email": "kavya.chowdhury@example.com",
    "phone": "164-827-3330",
    "ATS_score": 13,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "SQL"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Arjun Reddy",
    "email": "arjun.reddy@gmail.com",
    "phone": "421-961-1153",
    "ATS_score": 13,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "Rust"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Sai Kapoor",
    "email": "sai.kapoor@yahoo.com",
    "phone": "921-195-6873",
    "ATS_score": 14,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Flask"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Reyansh Roy",
    "email": "reyansh.roy@yahoo.com",
    "phone": "505-868-4635",
    "ATS_score": 14,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "SQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ananya Pillai",
    "email": "ananya.pillai@gmail.com",
    "phone": "650-257-3621",
    "ATS_score": 14,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Node.js"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Krishna Jain",
    "email": "krishna.jain@yahoo.com",
    "phone": "521-656-2310",
    "ATS_score": 14,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "NoSQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Reyansh Iyer",
    "email": "reyansh.iyer@example.com",
    "phone": "592-821-5300",
    "ATS_score": 14,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ayaan Kumar",
    "email": "ayaan.kumar@yahoo.com",
    "phone": "706-744-8436",
    "ATS_score": 14,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Digital Solutions",
    "skills": [
      "AWS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vivaan Patel",
    "email": "vivaan.patel@outlook.com",
    "phone": "247-403-5340",
    "ATS_score": 14,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "NexGen",
    "skills": [
      "Git"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Diya Joshi",
    "email": "diya.joshi@yahoo.com",
    "phone": "904-162-1657",
    "ATS_score": 14,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "TechCorp",
    "skills": [
      "Python"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Diya Singh",
    "email": "diya.singh@outlook.com",
    "phone": "530-488-8048",
    "ATS_score": 14,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "C#"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ayaan Kapoor",
    "email": "ayaan.kapoor@gmail.com",
    "phone": "732-260-4108",
    "ATS_score": 14,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "TechCorp",
    "skills": [
      "Rust"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Kavya Sharma",
    "email": "kavya.sharma@gmail.com",
    "phone": "528-103-8434",
    "ATS_score": 15,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "GraphQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Sara Menon",
    "email": "sara.menon@gmail.com",
    "phone": "662-458-9290",
    "ATS_score": 15,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Agile"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Reyansh Reddy",
    "email": "reyansh.reddy@gmail.com",
    "phone": "482-562-9623",
    "ATS_score": 15,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "TechWave",
    "skills": [
      "Flask"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarav Kumar",
    "email": "aarav.kumar@outlook.com",
    "phone": "129-657-8764",
    "ATS_score": 15,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Azure"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Reyansh Chowdhury",
    "email": "reyansh.chowdhury@example.com",
    "phone": "336-259-2670",
    "ATS_score": 15,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Saanvi Kumar",
    "email": "saanvi.kumar@gmail.com",
    "phone": "735-866-7707",
    "ATS_score": 15,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "SoftSys",
    "skills": [
      "NoSQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Priya Iyer",
    "email": "priya.iyer@example.com",
    "phone": "872-609-4297",
    "ATS_score": 15,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "FutureTech",
    "skills": [
      "Data Science"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Myra Menon",
    "email": "myra.menon@yahoo.com",
    "phone": "871-659-6416",
    "ATS_score": 15,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Git"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Kavya Gupta",
    "email": "kavya.gupta@yahoo.com",
    "phone": "574-136-4078",
    "ATS_score": 15,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Node.js"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@yahoo.com",
    "phone": "723-448-7033",
    "ATS_score": 15,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "Spring"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Intern"
  },
  {
    "name": "Diya Das",
    "email": "diya.das@gmail.com",
    "phone": "757-481-6435",
    "ATS_score": 16,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "AlphaTech",
    "skills": [
      "NoSQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Kavya Chopra",
    "email": "kavya.chopra@gmail.com",
    "phone": "926-160-7939",
    "ATS_score": 16,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "C#"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Avni Kumar",
    "email": "avni.kumar@yahoo.com",
    "phone": "512-126-8286",
    "ATS_score": 16,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Spring"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Saanvi Menon",
    "email": "saanvi.menon@gmail.com",
    "phone": "821-270-2631",
    "ATS_score": 16,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Angular"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Vihaan Chopra",
    "email": "vihaan.chopra@example.com",
    "phone": "127-445-4177",
    "ATS_score": 16,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Azure"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Gupta",
    "email": "sara.gupta@example.com",
    "phone": "516-398-9054",
    "ATS_score": 16,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Java"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Myra Jain",
    "email": "myra.jain@example.com",
    "phone": "224-484-6896",
    "ATS_score": 16,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Azure"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Vihaan Kumar",
    "email": "vihaan.kumar@outlook.com",
    "phone": "975-613-7210",
    "ATS_score": 16,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Flask"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Vihaan Nair",
    "email": "vihaan.nair@yahoo.com",
    "phone": "823-586-8098",
    "ATS_score": 16,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "DevOps"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Kavya Chopra",
    "email": "kavya.chopra@outlook.com",
    "phone": "883-364-1692",
    "ATS_score": 16,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "HTML"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Arjun Chowdhury",
    "email": "arjun.chowdhury@yahoo.com",
    "phone": "549-176-2100",
    "ATS_score": 17,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Data Science"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarav Joshi",
    "email": "aarav.joshi@gmail.com",
    "phone": "139-831-6729",
    "ATS_score": 17,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Spring"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ira Gupta",
    "email": "ira.gupta@yahoo.com",
    "phone": "262-270-8496",
    "ATS_score": 17,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Data Insights",
    "skills": [
      "AWS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Kavya Reddy",
    "email": "kavya.reddy@outlook.com",
    "phone": "512-728-4288",
    "ATS_score": 17,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "InnovateX",
    "skills": [
      "Scrum"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Game Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vihaan Chowdhury",
    "email": "vihaan.chowdhury@yahoo.com",
    "phone": "727-455-8547",
    "ATS_score": 17,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Ruby"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Sai Kapoor",
    "email": "sai.kapoor@outlook.com",
    "phone": "169-537-7925",
    "ATS_score": 17,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "AWS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Diya Kapoor",
    "email": "diya.kapoor@yahoo.com",
    "phone": "627-420-6843",
    "ATS_score": 17,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Git"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Kavya Patel",
    "email": "kavya.patel@outlook.com",
    "phone": "924-549-2541",
    "ATS_score": 17,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "InnovateX",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ishaan Chopra",
    "email": "ishaan.chopra@example.com",
    "phone": "702-962-6754",
    "ATS_score": 17,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "Go"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Sai Chowdhury",
    "email": "sai.chowdhury@yahoo.com",
    "phone": "243-514-5158",
    "ATS_score": 17,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Node.js"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Kavya Singh",
    "email": "kavya.singh@example.com",
    "phone": "370-980-3527",
    "ATS_score": 18,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Saanvi Chowdhury",
    "email": "saanvi.chowdhury@outlook.com",
    "phone": "260-340-1869",
    "ATS_score": 18,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "TypeScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Diya Iyer",
    "email": "diya.iyer@gmail.com",
    "phone": "172-831-1927",
    "ATS_score": 18,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "Spring"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sai Roy",
    "email": "sai.roy@outlook.com",
    "phone": "683-960-3710",
    "ATS_score": 18,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechCorp",
    "skills": [
      "Java"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Vivaan Sharma",
    "email": "vivaan.sharma@yahoo.com",
    "phone": "286-936-1307",
    "ATS_score": 18,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Creative Minds",
    "skills": [
      "JavaScript"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aarya Iyer",
    "email": "aarya.iyer@gmail.com",
    "phone": "799-113-7401",
    "ATS_score": 18,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "CSS"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Avni Singh",
    "email": "avni.singh@gmail.com",
    "phone": "556-430-4182",
    "ATS_score": 18,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Docker"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarav Chowdhury",
    "email": "aarav.chowdhury@gmail.com",
    "phone": "121-989-9049",
    "ATS_score": 18,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechCorp",
    "skills": [
      "DevOps"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aarya Kumar",
    "email": "aarya.kumar@outlook.com",
    "phone": "188-597-9156",
    "ATS_score": 18,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "DevSolutions",
    "skills": [
      "Django"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sai Mehta",
    "email": "sai.mehta@example.com",
    "phone": "728-654-6479",
    "ATS_score": 18,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Azure"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Diya Joshi",
    "email": "diya.joshi@yahoo.com",
    "phone": "291-594-5594",
    "ATS_score": 19,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "CSS"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vihaan Chopra",
    "email": "vihaan.chopra@example.com",
    "phone": "948-523-6395",
    "ATS_score": 19,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Flask"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Kavya Verma",
    "email": "kavya.verma@outlook.com",
    "phone": "319-765-1721",
    "ATS_score": 19,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Scrum"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Myra Gupta",
    "email": "myra.gupta@example.com",
    "phone": "940-365-1137",
    "ATS_score": 19,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Data Science"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Kavya Patel",
    "email": "kavya.patel@outlook.com",
    "phone": "448-936-3619",
    "ATS_score": 19,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "SQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Arjun Sharma",
    "email": "arjun.sharma@outlook.com",
    "phone": "269-918-5916",
    "ATS_score": 19,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "TechCorp",
    "skills": [
      "Go"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sai Iyer",
    "email": "sai.iyer@yahoo.com",
    "phone": "134-408-3384",
    "ATS_score": 19,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "JavaScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Saanvi Sharma",
    "email": "saanvi.sharma@example.com",
    "phone": "495-178-8200",
    "ATS_score": 19,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aditya Kumar",
    "email": "aditya.kumar@gmail.com",
    "phone": "936-734-4776",
    "ATS_score": 19,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Creative Minds",
    "skills": [
      "React"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ira Jain",
    "email": "ira.jain@outlook.com",
    "phone": "884-182-7940",
    "ATS_score": 19,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Agile"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Arjun Roy",
    "email": "arjun.roy@outlook.com",
    "phone": "465-762-4860",
    "ATS_score": 20,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Spring"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Myra Roy",
    "email": "myra.roy@gmail.com",
    "phone": "501-226-1849",
    "ATS_score": 20,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "GraphQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Diya Singh",
    "email": "diya.singh@example.com",
    "phone": "634-723-1669",
    "ATS_score": 20,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Flask",
      "Java"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Priya Mehta",
    "email": "priya.mehta@gmail.com",
    "phone": "320-414-7304",
    "ATS_score": 20,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "Docker",
      "Java"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ira Menon",
    "email": "ira.menon@yahoo.com",
    "phone": "710-921-4524",
    "ATS_score": 20,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Node.js",
      "JavaScript"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Vihaan Sharma",
    "email": "vihaan.sharma@outlook.com",
    "phone": "870-818-7891",
    "ATS_score": 20,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "Rust"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Myra Verma",
    "email": "myra.verma@yahoo.com",
    "phone": "443-261-7884",
    "ATS_score": 20,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "Docker"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Priya Patel",
    "email": "priya.patel@outlook.com",
    "phone": "962-330-5655",
    "ATS_score": 20,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "JavaScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Saanvi Verma",
    "email": "saanvi.verma@yahoo.com",
    "phone": "212-371-8475",
    "ATS_score": 20,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "SQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Krishna Gupta",
    "email": "krishna.gupta@yahoo.com",
    "phone": "449-240-7412",
    "ATS_score": 20,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Git",
      "Node.js"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Krishna Pillai",
    "email": "krishna.pillai@gmail.com",
    "phone": "810-149-7037",
    "ATS_score": 21,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "TechWave",
    "skills": [
      "AWS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ananya Menon",
    "email": "ananya.menon@gmail.com",
    "phone": "657-372-9986",
    "ATS_score": 21,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Azure",
      "Vue"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ira Iyer",
    "email": "ira.iyer@outlook.com",
    "phone": "837-775-5135",
    "ATS_score": 21,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "JavaScript",
      "Machine Learning"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Vihaan Das",
    "email": "vihaan.das@yahoo.com",
    "phone": "351-508-5840",
    "ATS_score": 21,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Java"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ira Reddy",
    "email": "ira.reddy@gmail.com",
    "phone": "639-105-9897",
    "ATS_score": 21,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Data Science"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Myra Kumar",
    "email": "myra.kumar@example.com",
    "phone": "535-993-8328",
    "ATS_score": 21,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "Machine Learning",
      "Go"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Sharma",
    "email": "avni.sharma@yahoo.com",
    "phone": "279-928-6659",
    "ATS_score": 21,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "SQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Vihaan Das",
    "email": "vihaan.das@yahoo.com",
    "phone": "122-435-2076",
    "ATS_score": 21,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "HTML",
      "Java"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aditya Reddy",
    "email": "aditya.reddy@outlook.com",
    "phone": "887-477-4603",
    "ATS_score": 21,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Rust"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Aarav Chopra",
    "email": "aarav.chopra@yahoo.com",
    "phone": "937-757-1420",
    "ATS_score": 21,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "JavaScript",
      "Rust"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Menon",
    "email": "krishna.menon@yahoo.com",
    "phone": "721-373-7917",
    "ATS_score": 22,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Spring"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Diya Reddy",
    "email": "diya.reddy@example.com",
    "phone": "949-195-4978",
    "ATS_score": 22,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "GraphQL",
      "Kubernetes"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Aarav Das",
    "email": "aarav.das@yahoo.com",
    "phone": "157-868-6824",
    "ATS_score": 22,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Data Insights",
    "skills": [
      "Agile"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarav Chowdhury",
    "email": "aarav.chowdhury@example.com",
    "phone": "793-910-3325",
    "ATS_score": 22,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "FutureTech",
    "skills": [
      "Kubernetes",
      "Node.js"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarav Iyer",
    "email": "aarav.iyer@gmail.com",
    "phone": "214-640-2101",
    "ATS_score": 22,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "Docker"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Vihaan Joshi",
    "email": "vihaan.joshi@yahoo.com",
    "phone": "107-688-4870",
    "ATS_score": 22,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "DevOps"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Kavya Das",
    "email": "kavya.das@outlook.com",
    "phone": "672-868-7713",
    "ATS_score": 22,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "JavaScript",
      "Python"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Vihaan Nair",
    "email": "vihaan.nair@outlook.com",
    "phone": "259-575-4087",
    "ATS_score": 22,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "FutureTech",
    "skills": [
      "Docker"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Joshi",
    "email": "ayaan.joshi@example.com",
    "phone": "235-376-2820",
    "ATS_score": 22,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Agile"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Kavya Joshi",
    "email": "kavya.joshi@yahoo.com",
    "phone": "754-859-6610",
    "ATS_score": 22,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Creative Minds",
    "skills": [
      "SQL",
      "GraphQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Kavya Singh",
    "email": "kavya.singh@gmail.com",
    "phone": "320-125-9940",
    "ATS_score": 23,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Flask",
      "Ruby"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vihaan Bhat",
    "email": "vihaan.bhat@gmail.com",
    "phone": "234-322-7112",
    "ATS_score": 23,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "DevOps"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Arjun Singh",
    "email": "arjun.singh@gmail.com",
    "phone": "879-105-2435",
    "ATS_score": 23,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Scrum"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Jain",
    "email": "krishna.jain@yahoo.com",
    "phone": "245-110-8172",
    "ATS_score": 23,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "React"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarav Gupta",
    "email": "aarav.gupta@gmail.com",
    "phone": "146-138-6168",
    "ATS_score": 23,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Scrum"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ira Chopra",
    "email": "ira.chopra@example.com",
    "phone": "877-957-4936",
    "ATS_score": 23,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "NoSQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Avni Sharma",
    "email": "avni.sharma@yahoo.com",
    "phone": "299-280-3304",
    "ATS_score": 23,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechCorp",
    "skills": [
      "AWS"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Kavya Chopra",
    "email": "kavya.chopra@example.com",
    "phone": "469-892-3552",
    "ATS_score": 23,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Creative Minds",
    "skills": [
      "GraphQL",
      "DevOps"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ayaan Iyer",
    "email": "ayaan.iyer@gmail.com",
    "phone": "192-606-9395",
    "ATS_score": 23,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "DataWorks",
    "skills": [
      "Git",
      "Scrum"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vivaan Kumar",
    "email": "vivaan.kumar@yahoo.com",
    "phone": "972-284-5768",
    "ATS_score": 23,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "JavaScript",
      "Go"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Priya Roy",
    "email": "priya.roy@example.com",
    "phone": "455-741-5023",
    "ATS_score": 24,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Vue",
      "React"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Vihaan Roy",
    "email": "vihaan.roy@example.com",
    "phone": "610-260-8685",
    "ATS_score": 24,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "SQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Project Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarav Patel",
    "email": "aarav.patel@yahoo.com",
    "phone": "866-602-1986",
    "ATS_score": 24,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "C#"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Intern"
  },
  {
    "name": "Diya Roy",
    "email": "diya.roy@outlook.com",
    "phone": "136-618-4985",
    "ATS_score": 24,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Global Solutions",
    "skills": [
      "C#"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Diya Kumar",
    "email": "diya.kumar@gmail.com",
    "phone": "692-423-9588",
    "ATS_score": 24,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "Git"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Reyansh Chopra",
    "email": "reyansh.chopra@gmail.com",
    "phone": "618-463-1866",
    "ATS_score": 24,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "FutureTech",
    "skills": [
      "React"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Priya Iyer",
    "email": "priya.iyer@yahoo.com",
    "phone": "706-285-8734",
    "ATS_score": 24,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Angular"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Krishna Patel",
    "email": "krishna.patel@gmail.com",
    "phone": "655-269-3401",
    "ATS_score": 24,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "Flask"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Reyansh Iyer",
    "email": "reyansh.iyer@example.com",
    "phone": "179-729-9460",
    "ATS_score": 24,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "Scrum",
      "Kubernetes"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Project Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sara Chowdhury",
    "email": "sara.chowdhury@outlook.com",
    "phone": "175-312-3783",
    "ATS_score": 24,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Git"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Saanvi Singh",
    "email": "saanvi.singh@example.com",
    "phone": "172-957-7939",
    "ATS_score": 25,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Go",
      "Java"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aditya Roy",
    "email": "aditya.roy@outlook.com",
    "phone": "880-438-7548",
    "ATS_score": 25,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "HTML"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Menon",
    "email": "krishna.menon@example.com",
    "phone": "119-581-9211",
    "ATS_score": 25,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Scrum"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Kavya Reddy",
    "email": "kavya.reddy@yahoo.com",
    "phone": "170-590-7560",
    "ATS_score": 25,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "CSS"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ayaan Gupta",
    "email": "ayaan.gupta@yahoo.com",
    "phone": "104-869-1199",
    "ATS_score": 25,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "C#"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ira Kumar",
    "email": "ira.kumar@gmail.com",
    "phone": "204-858-5643",
    "ATS_score": 25,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "FutureTech",
    "skills": [
      "C#",
      "Kubernetes"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Diya Joshi",
    "email": "diya.joshi@example.com",
    "phone": "234-596-4233",
    "ATS_score": 25,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Node.js"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Kavya Verma",
    "email": "kavya.verma@outlook.com",
    "phone": "866-945-5011",
    "ATS_score": 25,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "SQL",
      "Machine Learning"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sai Kapoor",
    "email": "sai.kapoor@outlook.com",
    "phone": "468-541-8022",
    "ATS_score": 25,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Django",
      "HTML"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Diya Reddy",
    "email": "diya.reddy@gmail.com",
    "phone": "125-567-9955",
    "ATS_score": 25,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Node.js"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Sara Menon",
    "email": "sara.menon@outlook.com",
    "phone": "836-713-7861",
    "ATS_score": 26,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarya Patel",
    "email": "aarya.patel@example.com",
    "phone": "771-663-1923",
    "ATS_score": 26,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Global Solutions",
    "skills": [
      "Angular"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Krishna Menon",
    "email": "krishna.menon@gmail.com",
    "phone": "176-247-5183",
    "ATS_score": 26,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "NoSQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Arjun Nair",
    "email": "arjun.nair@outlook.com",
    "phone": "611-444-5343",
    "ATS_score": 26,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Data Insights",
    "skills": [
      "Spring"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Avni Patel",
    "email": "avni.patel@gmail.com",
    "phone": "848-185-9042",
    "ATS_score": 26,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Flask",
      "Go"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Krishna Gupta",
    "email": "krishna.gupta@outlook.com",
    "phone": "503-603-6006",
    "ATS_score": 26,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Go"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sara Chowdhury",
    "email": "sara.chowdhury@outlook.com",
    "phone": "941-986-1299",
    "ATS_score": 26,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Flask",
      "Git"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aditya Verma",
    "email": "aditya.verma@gmail.com",
    "phone": "879-886-2631",
    "ATS_score": 26,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Node.js"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aarya Bhat",
    "email": "aarya.bhat@gmail.com",
    "phone": "602-509-8481",
    "ATS_score": 26,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Data Insights",
    "skills": [
      "Azure",
      "Django"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aditya Chowdhury",
    "email": "aditya.chowdhury@outlook.com",
    "phone": "544-896-8059",
    "ATS_score": 26,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Agile"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ananya Chopra",
    "email": "ananya.chopra@yahoo.com",
    "phone": "287-321-5146",
    "ATS_score": 27,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SmartTech",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aditya Kumar",
    "email": "aditya.kumar@gmail.com",
    "phone": "855-423-5518",
    "ATS_score": 27,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Java"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Saanvi Singh",
    "email": "saanvi.singh@yahoo.com",
    "phone": "411-899-6274",
    "ATS_score": 27,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "FutureTech",
    "skills": [
      "Docker",
      "Django"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ayaan Sharma",
    "email": "ayaan.sharma@gmail.com",
    "phone": "892-291-2523",
    "ATS_score": 27,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "TypeScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Priya Patel",
    "email": "priya.patel@outlook.com",
    "phone": "573-148-5031",
    "ATS_score": 27,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Angular"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Arjun Gupta",
    "email": "arjun.gupta@example.com",
    "phone": "197-501-3822",
    "ATS_score": 27,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Django",
      "GraphQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Kavya Roy",
    "email": "kavya.roy@gmail.com",
    "phone": "332-646-9672",
    "ATS_score": 27,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "TechWave",
    "skills": [
      "Rust"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Reyansh Pillai",
    "email": "reyansh.pillai@outlook.com",
    "phone": "292-926-3844",
    "ATS_score": 27,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Arjun Joshi",
    "email": "arjun.joshi@yahoo.com",
    "phone": "614-959-5038",
    "ATS_score": 27,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "JavaScript"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Arjun Patel",
    "email": "arjun.patel@example.com",
    "phone": "730-950-2060",
    "ATS_score": 27,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "C#"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarav Gupta",
    "email": "aarav.gupta@outlook.com",
    "phone": "910-881-2796",
    "ATS_score": 28,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Kubernetes",
      "Data Science"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sai Sharma",
    "email": "sai.sharma@gmail.com",
    "phone": "657-827-1198",
    "ATS_score": 28,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Spring",
      "Docker"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarya Patel",
    "email": "aarya.patel@gmail.com",
    "phone": "381-728-4509",
    "ATS_score": 28,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "GraphQL",
      "Scrum"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Kavya Das",
    "email": "kavya.das@gmail.com",
    "phone": "807-718-2609",
    "ATS_score": 28,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ananya Das",
    "email": "ananya.das@example.com",
    "phone": "137-722-1634",
    "ATS_score": 28,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechCorp",
    "skills": [
      "Git",
      "Rust"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Myra Bhat",
    "email": "myra.bhat@outlook.com",
    "phone": "400-153-9505",
    "ATS_score": 28,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "SQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aditya Menon",
    "email": "aditya.menon@example.com",
    "phone": "373-197-4240",
    "ATS_score": 28,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "DevOps",
      "Rust"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarya Pillai",
    "email": "aarya.pillai@yahoo.com",
    "phone": "485-225-1210",
    "ATS_score": 28,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "C#"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aarav Kapoor",
    "email": "aarav.kapoor@yahoo.com",
    "phone": "939-540-4417",
    "ATS_score": 28,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "Git"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Krishna Iyer",
    "email": "krishna.iyer@yahoo.com",
    "phone": "169-675-2039",
    "ATS_score": 28,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Angular"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Vivaan Reddy",
    "email": "vivaan.reddy@example.com",
    "phone": "442-792-4102",
    "ATS_score": 29,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DevSolutions",
    "skills": [
      "CSS",
      "Vue"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Gupta",
    "email": "avni.gupta@example.com",
    "phone": "997-101-1762",
    "ATS_score": 29,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Node.js"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ishaan Joshi",
    "email": "ishaan.joshi@gmail.com",
    "phone": "355-283-4715",
    "ATS_score": 29,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Kubernetes",
      "Docker"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Roy",
    "email": "sara.roy@example.com",
    "phone": "680-344-5698",
    "ATS_score": 29,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "AlphaTech",
    "skills": [
      "TypeScript"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aditya Chopra",
    "email": "aditya.chopra@yahoo.com",
    "phone": "306-507-5575",
    "ATS_score": 29,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechCorp",
    "skills": [
      "AWS"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aarav Patel",
    "email": "aarav.patel@gmail.com",
    "phone": "171-407-4457",
    "ATS_score": 29,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "Git"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ishaan Reddy",
    "email": "ishaan.reddy@outlook.com",
    "phone": "559-993-4790",
    "ATS_score": 29,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechCorp",
    "skills": [
      "Flask"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ayaan Gupta",
    "email": "ayaan.gupta@gmail.com",
    "phone": "218-732-2847",
    "ATS_score": 29,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Python"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Diya Das",
    "email": "diya.das@example.com",
    "phone": "993-160-6944",
    "ATS_score": 29,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aditya Pillai",
    "email": "aditya.pillai@example.com",
    "phone": "100-727-5996",
    "ATS_score": 29,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Python"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Vivaan Chopra",
    "email": "vivaan.chopra@outlook.com",
    "phone": "945-948-8387",
    "ATS_score": 30,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Flask"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sara Iyer",
    "email": "sara.iyer@outlook.com",
    "phone": "262-531-7085",
    "ATS_score": 30,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "TechWave",
    "skills": [
      "Rust",
      "Ruby"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ayaan Sharma",
    "email": "ayaan.sharma@yahoo.com",
    "phone": "699-167-5792",
    "ATS_score": 30,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Git"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ayaan Menon",
    "email": "ayaan.menon@example.com",
    "phone": "925-911-2522",
    "ATS_score": 30,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Git"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Reyansh Menon",
    "email": "reyansh.menon@gmail.com",
    "phone": "436-828-4726",
    "ATS_score": 30,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Vue"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Sara Jain",
    "email": "sara.jain@yahoo.com",
    "phone": "456-351-1730",
    "ATS_score": 30,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "CSS"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Diya Verma",
    "email": "diya.verma@outlook.com",
    "phone": "539-314-3470",
    "ATS_score": 30,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "DevSolutions",
    "skills": [
      "C#",
      "Kubernetes",
      "Python"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarav Verma",
    "email": "aarav.verma@yahoo.com",
    "phone": "869-610-9271",
    "ATS_score": 30,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "TypeScript",
      "Spring",
      "Flask"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Kavya Patel",
    "email": "kavya.patel@example.com",
    "phone": "307-460-8599",
    "ATS_score": 30,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "TypeScript",
      "Django"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ishaan Kapoor",
    "email": "ishaan.kapoor@outlook.com",
    "phone": "119-864-6662",
    "ATS_score": 30,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "Python",
      "React",
      "NoSQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Diya Gupta",
    "email": "diya.gupta@yahoo.com",
    "phone": "426-682-6779",
    "ATS_score": 31,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Ruby",
      "HTML"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarya Menon",
    "email": "aarya.menon@example.com",
    "phone": "555-629-8658",
    "ATS_score": 31,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "C#",
      "Node.js",
      "Docker"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarya Jain",
    "email": "aarya.jain@example.com",
    "phone": "438-176-6913",
    "ATS_score": 31,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Ruby"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ayaan Jain",
    "email": "ayaan.jain@outlook.com",
    "phone": "950-759-4848",
    "ATS_score": 31,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "C#"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Sara Jain",
    "email": "sara.jain@gmail.com",
    "phone": "636-330-6788",
    "ATS_score": 31,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Flask"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Reyansh Iyer",
    "email": "reyansh.iyer@yahoo.com",
    "phone": "982-866-8815",
    "ATS_score": 31,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "NoSQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aarya Iyer",
    "email": "aarya.iyer@yahoo.com",
    "phone": "758-155-8174",
    "ATS_score": 31,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Ruby",
      "TypeScript"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Reyansh Gupta",
    "email": "reyansh.gupta@gmail.com",
    "phone": "159-197-7809",
    "ATS_score": 31,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Global Solutions",
    "skills": [
      "TypeScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Diya Verma",
    "email": "diya.verma@example.com",
    "phone": "883-453-1700",
    "ATS_score": 31,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "DevOps"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Krishna Jain",
    "email": "krishna.jain@example.com",
    "phone": "701-711-2755",
    "ATS_score": 31,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Rust",
      "Angular",
      "HTML"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarya Roy",
    "email": "aarya.roy@example.com",
    "phone": "950-336-5394",
    "ATS_score": 32,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "TechCorp",
    "skills": [
      "Azure"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Saanvi Reddy",
    "email": "saanvi.reddy@gmail.com",
    "phone": "427-294-3504",
    "ATS_score": 32,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Vue"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Reyansh Joshi",
    "email": "reyansh.joshi@example.com",
    "phone": "523-658-7608",
    "ATS_score": 32,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Kavya Pillai",
    "email": "kavya.pillai@yahoo.com",
    "phone": "187-557-1489",
    "ATS_score": 32,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "TypeScript",
      "Node.js",
      "Angular"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ananya Das",
    "email": "ananya.das@yahoo.com",
    "phone": "773-621-9365",
    "ATS_score": 32,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Agile"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Diya Patel",
    "email": "diya.patel@example.com",
    "phone": "372-246-1870",
    "ATS_score": 32,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "Node.js",
      "TypeScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aarav Reddy",
    "email": "aarav.reddy@yahoo.com",
    "phone": "309-192-7942",
    "ATS_score": 32,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "JavaScript"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ananya Gupta",
    "email": "ananya.gupta@yahoo.com",
    "phone": "191-345-3351",
    "ATS_score": 32,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "TechWave",
    "skills": [
      "Azure"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Arjun Verma",
    "email": "arjun.verma@yahoo.com",
    "phone": "591-835-3355",
    "ATS_score": 32,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Agile"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sai Singh",
    "email": "sai.singh@yahoo.com",
    "phone": "589-621-4374",
    "ATS_score": 32,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "TechCorp",
    "skills": [
      "JavaScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aditya Patel",
    "email": "aditya.patel@gmail.com",
    "phone": "256-943-2332",
    "ATS_score": 33,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "InnovateX",
    "skills": [
      "NoSQL",
      "Go",
      "AWS"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Aarya Kumar",
    "email": "aarya.kumar@yahoo.com",
    "phone": "578-321-1342",
    "ATS_score": 33,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "CSS",
      "NoSQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Saanvi Chopra",
    "email": "saanvi.chopra@example.com",
    "phone": "664-819-8951",
    "ATS_score": 33,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "DataWorks",
    "skills": [
      "Git"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Kavya Menon",
    "email": "kavya.menon@gmail.com",
    "phone": "328-896-8485",
    "ATS_score": 33,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "NoSQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Arjun Chopra",
    "email": "arjun.chopra@outlook.com",
    "phone": "491-572-1913",
    "ATS_score": 33,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "JavaScript",
      "Vue"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ishaan Iyer",
    "email": "ishaan.iyer@gmail.com",
    "phone": "154-651-2141",
    "ATS_score": 33,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Node.js"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Vihaan Sharma",
    "email": "vihaan.sharma@outlook.com",
    "phone": "112-546-3463",
    "ATS_score": 33,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "AWS"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ira Pillai",
    "email": "ira.pillai@outlook.com",
    "phone": "242-585-9075",
    "ATS_score": 33,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Reyansh Reddy",
    "email": "reyansh.reddy@outlook.com",
    "phone": "927-414-7163",
    "ATS_score": 33,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Flask"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Product Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sai Menon",
    "email": "sai.menon@outlook.com",
    "phone": "579-302-9410",
    "ATS_score": 33,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "HTML"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aditya Sharma",
    "email": "aditya.sharma@example.com",
    "phone": "457-114-6784",
    "ATS_score": 34,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "NexGen",
    "skills": [
      "Ruby",
      "SQL",
      "Flask"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Reyansh Kumar",
    "email": "reyansh.kumar@gmail.com",
    "phone": "972-334-4148",
    "ATS_score": 34,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "SoftSys",
    "skills": [
      "CSS"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Vihaan Menon",
    "email": "vihaan.menon@outlook.com",
    "phone": "218-212-4225",
    "ATS_score": 34,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "SQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ananya Das",
    "email": "ananya.das@yahoo.com",
    "phone": "972-424-9498",
    "ATS_score": 34,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Vue",
      "Agile"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Saanvi Verma",
    "email": "saanvi.verma@outlook.com",
    "phone": "958-979-9334",
    "ATS_score": 34,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "DataWorks",
    "skills": [
      "GraphQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ayaan Reddy",
    "email": "ayaan.reddy@outlook.com",
    "phone": "960-320-9311",
    "ATS_score": 34,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "InnovateX",
    "skills": [
      "GraphQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Saanvi Chowdhury",
    "email": "saanvi.chowdhury@yahoo.com",
    "phone": "400-396-8350",
    "ATS_score": 34,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "FutureTech",
    "skills": [
      "Rust",
      "Data Science"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Kavya Patel",
    "email": "kavya.patel@example.com",
    "phone": "453-804-6220",
    "ATS_score": 34,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "GraphQL",
      "NoSQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Diya Kumar",
    "email": "diya.kumar@example.com",
    "phone": "101-926-2460",
    "ATS_score": 34,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "CodeCrafters",
    "skills": [
      "DevOps",
      "Django",
      "NoSQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ira Patel",
    "email": "ira.patel@yahoo.com",
    "phone": "109-531-6300",
    "ATS_score": 34,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Django",
      "Go"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ayaan Joshi",
    "email": "ayaan.joshi@gmail.com",
    "phone": "794-863-9293",
    "ATS_score": 35,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "InnovateX",
    "skills": [
      "Data Science"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ayaan Kapoor",
    "email": "ayaan.kapoor@gmail.com",
    "phone": "107-822-7605",
    "ATS_score": 35,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Rust",
      "DevOps"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Myra Menon",
    "email": "myra.menon@gmail.com",
    "phone": "853-622-1366",
    "ATS_score": 35,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Go"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Saanvi Kapoor",
    "email": "saanvi.kapoor@yahoo.com",
    "phone": "514-381-2950",
    "ATS_score": 35,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "InnovateX",
    "skills": [
      "CSS",
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Krishna Sharma",
    "email": "krishna.sharma@example.com",
    "phone": "346-283-1178",
    "ATS_score": 35,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Python"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Kavya Roy",
    "email": "kavya.roy@gmail.com",
    "phone": "587-271-3325",
    "ATS_score": 35,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarya Gupta",
    "email": "aarya.gupta@yahoo.com",
    "phone": "324-987-5117",
    "ATS_score": 35,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Docker"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Saanvi Iyer",
    "email": "saanvi.iyer@gmail.com",
    "phone": "515-923-2265",
    "ATS_score": 35,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "FutureTech",
    "skills": [
      "Docker",
      "GraphQL",
      "Vue"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Sara Mehta",
    "email": "sara.mehta@outlook.com",
    "phone": "376-737-1944",
    "ATS_score": 35,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Flask",
      "Ruby",
      "NoSQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vivaan Menon",
    "email": "vivaan.menon@outlook.com",
    "phone": "857-465-8681",
    "ATS_score": 35,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Docker"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Kavya Patel",
    "email": "kavya.patel@yahoo.com",
    "phone": "392-509-5506",
    "ATS_score": 36,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Docker"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vihaan Sharma",
    "email": "vihaan.sharma@example.com",
    "phone": "997-126-1924",
    "ATS_score": 36,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "NoSQL",
      "Kubernetes",
      "Go"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sai Bhat",
    "email": "sai.bhat@outlook.com",
    "phone": "474-300-9279",
    "ATS_score": 36,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "DevSolutions",
    "skills": [
      "TypeScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Avni Gupta",
    "email": "avni.gupta@gmail.com",
    "phone": "483-896-2558",
    "ATS_score": 36,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "FutureTech",
    "skills": [
      "Flask"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Vihaan Reddy",
    "email": "vihaan.reddy@yahoo.com",
    "phone": "328-211-1084",
    "ATS_score": 36,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Global Solutions",
    "skills": [
      "Django",
      "Machine Learning"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Aarya Nair",
    "email": "aarya.nair@yahoo.com",
    "phone": "377-296-5414",
    "ATS_score": 36,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Creative Minds",
    "skills": [
      "SQL",
      "AWS"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Saanvi Roy",
    "email": "saanvi.roy@gmail.com",
    "phone": "111-807-4404",
    "ATS_score": 36,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Data Science"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Kavya Chowdhury",
    "email": "kavya.chowdhury@example.com",
    "phone": "808-939-5149",
    "ATS_score": 36,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Java",
      "Vue"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Myra Mehta",
    "email": "myra.mehta@yahoo.com",
    "phone": "772-841-9197",
    "ATS_score": 36,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "DataWorks",
    "skills": [
      "Django",
      "Data Science"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Diya Verma",
    "email": "diya.verma@gmail.com",
    "phone": "487-278-1757",
    "ATS_score": 36,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "Agile"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sara Pillai",
    "email": "sara.pillai@outlook.com",
    "phone": "546-182-7204",
    "ATS_score": 37,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "AWS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Vihaan Bhat",
    "email": "vihaan.bhat@yahoo.com",
    "phone": "161-886-5709",
    "ATS_score": 37,
    "yearsExperience": 4,
    "degree": "B.E Electronics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "CSS"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Verma",
    "email": "avni.verma@gmail.com",
    "phone": "585-361-1908",
    "ATS_score": 37,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Rust"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aarya Kapoor",
    "email": "aarya.kapoor@yahoo.com",
    "phone": "131-461-8565",
    "ATS_score": 37,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Spring"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ira Jain",
    "email": "ira.jain@outlook.com",
    "phone": "878-702-2275",
    "ATS_score": 37,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Agile",
      "C#",
      "TypeScript"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Diya Sharma",
    "email": "diya.sharma@example.com",
    "phone": "879-457-9471",
    "ATS_score": 37,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Vue"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Myra Kapoor",
    "email": "myra.kapoor@outlook.com",
    "phone": "225-404-2421",
    "ATS_score": 37,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Java",
      "Python",
      "Rust"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Sai Joshi",
    "email": "sai.joshi@example.com",
    "phone": "145-389-9042",
    "ATS_score": 37,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Python"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Saanvi Chowdhury",
    "email": "saanvi.chowdhury@gmail.com",
    "phone": "376-852-5868",
    "ATS_score": 37,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Rust",
      "AWS"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Vihaan Chopra",
    "email": "vihaan.chopra@outlook.com",
    "phone": "457-831-8021",
    "ATS_score": 37,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DevSolutions",
    "skills": [
      "Node.js"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Saanvi Joshi",
    "email": "saanvi.joshi@outlook.com",
    "phone": "767-527-5540",
    "ATS_score": 38,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "GraphQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Saanvi Chopra",
    "email": "saanvi.chopra@example.com",
    "phone": "503-943-9119",
    "ATS_score": 38,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "Azure"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ira Jain",
    "email": "ira.jain@gmail.com",
    "phone": "807-408-7038",
    "ATS_score": 38,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Priya Singh",
    "email": "priya.singh@yahoo.com",
    "phone": "519-104-7047",
    "ATS_score": 38,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "NoSQL",
      "Kubernetes",
      "Node.js"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aditya Nair",
    "email": "aditya.nair@example.com",
    "phone": "840-122-9631",
    "ATS_score": 38,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Vue",
      "React",
      "SQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Priya Jain",
    "email": "priya.jain@yahoo.com",
    "phone": "496-103-8599",
    "ATS_score": 38,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Java",
      "C#"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aditya Pillai",
    "email": "aditya.pillai@gmail.com",
    "phone": "818-288-7187",
    "ATS_score": 38,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "CSS"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Sara Verma",
    "email": "sara.verma@outlook.com",
    "phone": "508-260-5136",
    "ATS_score": 38,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Rust"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Avni Joshi",
    "email": "avni.joshi@yahoo.com",
    "phone": "818-142-7340",
    "ATS_score": 38,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "Node.js"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ishaan Jain",
    "email": "ishaan.jain@outlook.com",
    "phone": "227-668-5966",
    "ATS_score": 38,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "NexGen",
    "skills": [
      "Azure"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Gupta",
    "email": "avni.gupta@outlook.com",
    "phone": "734-564-8264",
    "ATS_score": 39,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "InnovateX",
    "skills": [
      "CSS",
      "Scrum"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarav Roy",
    "email": "aarav.roy@yahoo.com",
    "phone": "249-724-9650",
    "ATS_score": 39,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Angular"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Avni Patel",
    "email": "avni.patel@gmail.com",
    "phone": "786-828-8040",
    "ATS_score": 39,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Java",
      "NoSQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarav Chopra",
    "email": "aarav.chopra@yahoo.com",
    "phone": "515-238-3401",
    "ATS_score": 39,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Rust",
      "AWS"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vihaan Iyer",
    "email": "vihaan.iyer@gmail.com",
    "phone": "486-730-4110",
    "ATS_score": 39,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Java",
      "NoSQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ishaan Das",
    "email": "ishaan.das@yahoo.com",
    "phone": "896-428-5655",
    "ATS_score": 39,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "Docker",
      "HTML",
      "Rust"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Arjun Patel",
    "email": "arjun.patel@outlook.com",
    "phone": "195-574-5714",
    "ATS_score": 39,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechWave",
    "skills": [
      "Java",
      "Flask"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vivaan Chopra",
    "email": "vivaan.chopra@example.com",
    "phone": "921-253-6064",
    "ATS_score": 39,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "CSS",
      "TypeScript"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vihaan Reddy",
    "email": "vihaan.reddy@outlook.com",
    "phone": "316-748-8672",
    "ATS_score": 39,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Vue"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Myra Gupta",
    "email": "myra.gupta@gmail.com",
    "phone": "930-136-7887",
    "ATS_score": 39,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "FutureTech",
    "skills": [
      "Java"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Nair",
    "email": "ayaan.nair@example.com",
    "phone": "400-460-3641",
    "ATS_score": 40,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Java",
      "Go"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ananya Verma",
    "email": "ananya.verma@gmail.com",
    "phone": "599-397-7047",
    "ATS_score": 40,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "FutureTech",
    "skills": [
      "React",
      "Kubernetes"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Saanvi Jain",
    "email": "saanvi.jain@outlook.com",
    "phone": "122-576-2512",
    "ATS_score": 40,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "NoSQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Priya Nair",
    "email": "priya.nair@outlook.com",
    "phone": "366-816-8859",
    "ATS_score": 40,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Git",
      "Java",
      "JavaScript",
      "Django"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aarya Kapoor",
    "email": "aarya.kapoor@example.com",
    "phone": "959-596-7061",
    "ATS_score": 40,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sara Kumar",
    "email": "sara.kumar@outlook.com",
    "phone": "193-776-8701",
    "ATS_score": 40,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "GraphQL",
      "Flask",
      "Ruby"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarya Roy",
    "email": "aarya.roy@gmail.com",
    "phone": "543-119-2326",
    "ATS_score": 40,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "DevOps"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Project Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Reyansh Menon",
    "email": "reyansh.menon@example.com",
    "phone": "117-523-3968",
    "ATS_score": 40,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Node.js"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Aditya Iyer",
    "email": "aditya.iyer@gmail.com",
    "phone": "446-677-2697",
    "ATS_score": 40,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Machine Learning",
      "Java"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Sai Patel",
    "email": "sai.patel@example.com",
    "phone": "658-298-3284",
    "ATS_score": 40,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Django"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Saanvi Verma",
    "email": "saanvi.verma@gmail.com",
    "phone": "554-667-8258",
    "ATS_score": 41,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "GraphQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarav Nair",
    "email": "aarav.nair@example.com",
    "phone": "274-837-6320",
    "ATS_score": 41,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "CSS",
      "Git",
      "JavaScript",
      "HTML"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarav Chopra",
    "email": "aarav.chopra@gmail.com",
    "phone": "589-231-1151",
    "ATS_score": 41,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Flask",
      "JavaScript",
      "DevOps"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Intern"
  },
  {
    "name": "Sai Verma",
    "email": "sai.verma@outlook.com",
    "phone": "386-177-4316",
    "ATS_score": 41,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "GraphQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Kavya Chowdhury",
    "email": "kavya.chowdhury@example.com",
    "phone": "725-887-8621",
    "ATS_score": 41,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Data Science",
      "NoSQL",
      "Ruby"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Sara Chopra",
    "email": "sara.chopra@outlook.com",
    "phone": "416-507-8725",
    "ATS_score": 41,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Global Solutions",
    "skills": [
      "NoSQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Reyansh Gupta",
    "email": "reyansh.gupta@yahoo.com",
    "phone": "952-548-9848",
    "ATS_score": 41,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "SQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Vivaan Das",
    "email": "vivaan.das@outlook.com",
    "phone": "874-425-2979",
    "ATS_score": 41,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Django"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Avni Mehta",
    "email": "avni.mehta@example.com",
    "phone": "495-253-7698",
    "ATS_score": 41,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Go"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Game Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ananya Pillai",
    "email": "ananya.pillai@yahoo.com",
    "phone": "308-375-5473",
    "ATS_score": 41,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "DataWorks",
    "skills": [
      "Node.js"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sai Iyer",
    "email": "sai.iyer@example.com",
    "phone": "487-851-5962",
    "ATS_score": 42,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "GraphQL",
      "Node.js",
      "Agile"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Reyansh Menon",
    "email": "reyansh.menon@gmail.com",
    "phone": "202-724-6188",
    "ATS_score": 42,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Scrum",
      "Ruby",
      "Data Science"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Vivaan Patel",
    "email": "vivaan.patel@yahoo.com",
    "phone": "574-307-6158",
    "ATS_score": 42,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechCorp",
    "skills": [
      "Django",
      "NoSQL",
      "Docker",
      "Spring"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Arjun Bhat",
    "email": "arjun.bhat@outlook.com",
    "phone": "332-462-9727",
    "ATS_score": 42,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "Angular",
      "Go"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Priya Gupta",
    "email": "priya.gupta@gmail.com",
    "phone": "214-228-3509",
    "ATS_score": 42,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Ruby"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sai Kumar",
    "email": "sai.kumar@outlook.com",
    "phone": "464-831-7482",
    "ATS_score": 42,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "FutureTech",
    "skills": [
      "Spring",
      "HTML",
      "Java",
      "JavaScript"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ishaan Das",
    "email": "ishaan.das@yahoo.com",
    "phone": "311-963-3956",
    "ATS_score": 42,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "Vue",
      "Ruby"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Priya Patel",
    "email": "priya.patel@outlook.com",
    "phone": "191-414-1026",
    "ATS_score": 42,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "AWS",
      "JavaScript",
      "Machine Learning",
      "NoSQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Sai Chopra",
    "email": "sai.chopra@outlook.com",
    "phone": "412-273-2828",
    "ATS_score": 42,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "React"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarya Bhat",
    "email": "aarya.bhat@outlook.com",
    "phone": "244-581-4429",
    "ATS_score": 42,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "InnovateX",
    "skills": [
      "GraphQL",
      "SQL",
      "C#"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Avni Kapoor",
    "email": "avni.kapoor@example.com",
    "phone": "940-683-9189",
    "ATS_score": 43,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "JavaScript",
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ananya Roy",
    "email": "ananya.roy@outlook.com",
    "phone": "103-890-7008",
    "ATS_score": 43,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "Python"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarya Chowdhury",
    "email": "aarya.chowdhury@example.com",
    "phone": "247-498-2323",
    "ATS_score": 43,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "FutureTech",
    "skills": [
      "Agile"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Reyansh Reddy",
    "email": "reyansh.reddy@example.com",
    "phone": "799-116-8470",
    "ATS_score": 43,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "CSS",
      "TypeScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ishaan Gupta",
    "email": "ishaan.gupta@outlook.com",
    "phone": "560-572-1393",
    "ATS_score": 43,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Git"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ayaan Bhat",
    "email": "ayaan.bhat@outlook.com",
    "phone": "918-587-5297",
    "ATS_score": 43,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechCorp",
    "skills": [
      "Rust"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Priya Chowdhury",
    "email": "priya.chowdhury@gmail.com",
    "phone": "996-571-7848",
    "ATS_score": 43,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Java",
      "C#"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Kavya Singh",
    "email": "kavya.singh@outlook.com",
    "phone": "495-488-3159",
    "ATS_score": 43,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "InnovateX",
    "skills": [
      "Kubernetes",
      "GraphQL",
      "SQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ishaan Singh",
    "email": "ishaan.singh@example.com",
    "phone": "462-433-8888",
    "ATS_score": 43,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "Java",
      "Git"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Diya Menon",
    "email": "diya.menon@outlook.com",
    "phone": "817-287-4367",
    "ATS_score": 43,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "TechCorp",
    "skills": [
      "Rust",
      "AWS",
      "SQL",
      "Node.js"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sai Joshi",
    "email": "sai.joshi@outlook.com",
    "phone": "605-688-5711",
    "ATS_score": 44,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "DevOps"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ananya Sharma",
    "email": "ananya.sharma@yahoo.com",
    "phone": "153-701-3509",
    "ATS_score": 44,
    "yearsExperience": 4,
    "degree": "B.E Electronics",
    "previousCompany": "TechWave",
    "skills": [
      "Go"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Saanvi Verma",
    "email": "saanvi.verma@outlook.com",
    "phone": "587-978-8495",
    "ATS_score": 44,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "AWS",
      "C#",
      "Kubernetes",
      "TypeScript"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ayaan Verma",
    "email": "ayaan.verma@gmail.com",
    "phone": "211-541-8286",
    "ATS_score": 44,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "JavaScript"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Diya Iyer",
    "email": "diya.iyer@yahoo.com",
    "phone": "597-257-1140",
    "ATS_score": 44,
    "yearsExperience": 5,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "GraphQL",
      "Rust",
      "Machine Learning",
      "Kubernetes"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ayaan Pillai",
    "email": "ayaan.pillai@outlook.com",
    "phone": "706-454-7557",
    "ATS_score": 44,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "C#"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Myra Bhat",
    "email": "myra.bhat@yahoo.com",
    "phone": "673-217-5197",
    "ATS_score": 44,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Flask"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Sai Das",
    "email": "sai.das@gmail.com",
    "phone": "787-302-9887",
    "ATS_score": 44,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Flask"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Priya Sharma",
    "email": "priya.sharma@gmail.com",
    "phone": "278-351-3730",
    "ATS_score": 44,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Global Solutions",
    "skills": [
      "Machine Learning",
      "Django",
      "Node.js"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ira Mehta",
    "email": "ira.mehta@gmail.com",
    "phone": "536-284-8331",
    "ATS_score": 44,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "NexGen",
    "skills": [
      "Django",
      "Vue"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ananya Kapoor",
    "email": "ananya.kapoor@yahoo.com",
    "phone": "883-317-8300",
    "ATS_score": 45,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Scrum"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ayaan Singh",
    "email": "ayaan.singh@example.com",
    "phone": "418-294-3442",
    "ATS_score": 45,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "TechWave",
    "skills": [
      "SQL",
      "HTML"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Vihaan Sharma",
    "email": "vihaan.sharma@outlook.com",
    "phone": "629-934-5284",
    "ATS_score": 45,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "TechCorp",
    "skills": [
      "Scrum",
      "C#"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Avni Menon",
    "email": "avni.menon@example.com",
    "phone": "374-234-5405",
    "ATS_score": 45,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "SQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Sai Verma",
    "email": "sai.verma@example.com",
    "phone": "937-809-9068",
    "ATS_score": 45,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "HTML"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ira Iyer",
    "email": "ira.iyer@yahoo.com",
    "phone": "116-409-2660",
    "ATS_score": 45,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "SQL",
      "Vue",
      "Java"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ishaan Verma",
    "email": "ishaan.verma@gmail.com",
    "phone": "134-544-3720",
    "ATS_score": 45,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechCorp",
    "skills": [
      "Azure"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Myra Verma",
    "email": "myra.verma@yahoo.com",
    "phone": "940-782-3310",
    "ATS_score": 45,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Vue",
      "Flask",
      "Docker",
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@outlook.com",
    "phone": "820-526-6705",
    "ATS_score": 45,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Kubernetes",
      "CSS",
      "Go"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Krishna Verma",
    "email": "krishna.verma@outlook.com",
    "phone": "776-388-6535",
    "ATS_score": 45,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Azure",
      "Machine Learning"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Vivaan Patel",
    "email": "vivaan.patel@example.com",
    "phone": "651-329-2091",
    "ATS_score": 46,
    "yearsExperience": 5,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DevSolutions",
    "skills": [
      "Spring",
      "Git",
      "TypeScript"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vihaan Nair",
    "email": "vihaan.nair@outlook.com",
    "phone": "414-981-4462",
    "ATS_score": 46,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "CSS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sai Singh",
    "email": "sai.singh@outlook.com",
    "phone": "245-565-8942",
    "ATS_score": 46,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "CSS",
      "AWS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Reyansh Gupta",
    "email": "reyansh.gupta@gmail.com",
    "phone": "847-515-6546",
    "ATS_score": 46,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Angular",
      "Rust",
      "Vue",
      "Ruby"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ananya Pillai",
    "email": "ananya.pillai@example.com",
    "phone": "380-441-6851",
    "ATS_score": 46,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "HTML"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Vihaan Kumar",
    "email": "vihaan.kumar@outlook.com",
    "phone": "815-278-4455",
    "ATS_score": 46,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SmartTech",
    "skills": [
      "Go",
      "NoSQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Krishna Kapoor",
    "email": "krishna.kapoor@outlook.com",
    "phone": "796-192-2595",
    "ATS_score": 46,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Docker",
      "Angular"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Priya Reddy",
    "email": "priya.reddy@gmail.com",
    "phone": "910-210-6040",
    "ATS_score": 46,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Data Science",
      "NoSQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarav Das",
    "email": "aarav.das@example.com",
    "phone": "315-928-7925",
    "ATS_score": 46,
    "yearsExperience": 5,
    "degree": "B.E Electronics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Python"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Diya Iyer",
    "email": "diya.iyer@gmail.com",
    "phone": "435-108-2836",
    "ATS_score": 46,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "Azure",
      "Scrum"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ishaan Patel",
    "email": "ishaan.patel@outlook.com",
    "phone": "817-460-1533",
    "ATS_score": 47,
    "yearsExperience": 4,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "Git",
      "Rust"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aditya Reddy",
    "email": "aditya.reddy@example.com",
    "phone": "124-476-1862",
    "ATS_score": 47,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "FutureTech",
    "skills": [
      "Docker"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Vivaan Sharma",
    "email": "vivaan.sharma@gmail.com",
    "phone": "998-976-4652",
    "ATS_score": 47,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Scrum",
      "Rust"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarya Das",
    "email": "aarya.das@outlook.com",
    "phone": "912-988-7764",
    "ATS_score": 47,
    "yearsExperience": 5,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "HTML",
      "Django"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ananya Pillai",
    "email": "ananya.pillai@yahoo.com",
    "phone": "656-422-5683",
    "ATS_score": 47,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Docker"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Myra Chopra",
    "email": "myra.chopra@outlook.com",
    "phone": "759-730-5681",
    "ATS_score": 47,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "C#",
      "TypeScript"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Priya Kapoor",
    "email": "priya.kapoor@outlook.com",
    "phone": "473-855-6477",
    "ATS_score": 47,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Azure",
      "Docker",
      "Python"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ayaan Singh",
    "email": "ayaan.singh@outlook.com",
    "phone": "558-890-1956",
    "ATS_score": 47,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NexGen",
    "skills": [
      "Flask"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Avni Iyer",
    "email": "avni.iyer@yahoo.com",
    "phone": "175-713-5817",
    "ATS_score": 47,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Flask",
      "DevOps",
      "React"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Krishna Nair",
    "email": "krishna.nair@outlook.com",
    "phone": "608-815-6418",
    "ATS_score": 47,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "HTML",
      "CSS",
      "React",
      "Spring"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Aarav Kumar",
    "email": "aarav.kumar@outlook.com",
    "phone": "834-847-5064",
    "ATS_score": 48,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "TechCorp",
    "skills": [
      "Scrum",
      "Flask",
      "Spring",
      "AWS"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Kavya Roy",
    "email": "kavya.roy@gmail.com",
    "phone": "949-496-1127",
    "ATS_score": 48,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "InnovateX",
    "skills": [
      "TypeScript",
      "Node.js",
      "Angular",
      "HTML"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ishaan Mehta",
    "email": "ishaan.mehta@outlook.com",
    "phone": "716-563-8974",
    "ATS_score": 48,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Data Insights",
    "skills": [
      "Scrum",
      "React"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Kavya Kumar",
    "email": "kavya.kumar@gmail.com",
    "phone": "128-195-2323",
    "ATS_score": 48,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "React"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Myra Patel",
    "email": "myra.patel@yahoo.com",
    "phone": "926-509-4133",
    "ATS_score": 48,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Vue"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Arjun Iyer",
    "email": "arjun.iyer@gmail.com",
    "phone": "972-159-8303",
    "ATS_score": 48,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Spring"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Priya Bhat",
    "email": "priya.bhat@outlook.com",
    "phone": "848-843-2385",
    "ATS_score": 48,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Django"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Kavya Kumar",
    "email": "kavya.kumar@example.com",
    "phone": "980-721-3013",
    "ATS_score": 48,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "Go",
      "GraphQL",
      "JavaScript",
      "CSS"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ira Sharma",
    "email": "ira.sharma@yahoo.com",
    "phone": "233-197-7082",
    "ATS_score": 48,
    "yearsExperience": 5,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Vue",
      "Angular",
      "Spring"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Aarav Gupta",
    "email": "aarav.gupta@yahoo.com",
    "phone": "513-457-6597",
    "ATS_score": 48,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Angular",
      "Node.js"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Avni Nair",
    "email": "avni.nair@yahoo.com",
    "phone": "273-499-6885",
    "ATS_score": 49,
    "yearsExperience": 5,
    "degree": "B.E Electronics",
    "previousCompany": "Creative Minds",
    "skills": [
      "DevOps",
      "Angular",
      "Scrum",
      "CSS"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Sai Chopra",
    "email": "sai.chopra@outlook.com",
    "phone": "262-234-7369",
    "ATS_score": 49,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "AWS",
      "Vue",
      "DevOps",
      "CSS"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ishaan Joshi",
    "email": "ishaan.joshi@outlook.com",
    "phone": "750-942-6133",
    "ATS_score": 49,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "TypeScript",
      "Django"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ira Das",
    "email": "ira.das@example.com",
    "phone": "865-778-9687",
    "ATS_score": 49,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Data Science",
      "Kubernetes",
      "SQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Arjun Menon",
    "email": "arjun.menon@gmail.com",
    "phone": "410-136-2117",
    "ATS_score": 49,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "C#"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Vivaan Pillai",
    "email": "vivaan.pillai@gmail.com",
    "phone": "532-481-8553",
    "ATS_score": 49,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechWave",
    "skills": [
      "JavaScript"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Avni Patel",
    "email": "avni.patel@outlook.com",
    "phone": "834-146-8847",
    "ATS_score": 49,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "InnovateX",
    "skills": [
      "DevOps",
      "Django",
      "Docker"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Avni Verma",
    "email": "avni.verma@yahoo.com",
    "phone": "473-934-9829",
    "ATS_score": 49,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Docker",
      "Flask"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ira Mehta",
    "email": "ira.mehta@yahoo.com",
    "phone": "571-418-5781",
    "ATS_score": 49,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Django",
      "C#",
      "JavaScript",
      "Docker"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Reyansh Nair",
    "email": "reyansh.nair@outlook.com",
    "phone": "174-842-4948",
    "ATS_score": 49,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "React",
      "NoSQL",
      "AWS",
      "JavaScript"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aditya Patel",
    "email": "aditya.patel@yahoo.com",
    "phone": "724-960-1684",
    "ATS_score": 50,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Data Science"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ananya Menon",
    "email": "ananya.menon@example.com",
    "phone": "339-250-6655",
    "ATS_score": 50,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Data Insights",
    "skills": [
      "JavaScript",
      "Git"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ishaan Kapoor",
    "email": "ishaan.kapoor@example.com",
    "phone": "847-340-8324",
    "ATS_score": 50,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "SQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ishaan Gupta",
    "email": "ishaan.gupta@example.com",
    "phone": "697-559-6898",
    "ATS_score": 50,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "AWS"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Priya Patel",
    "email": "priya.patel@example.com",
    "phone": "121-383-9066",
    "ATS_score": 50,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Azure",
      "Docker",
      "TypeScript",
      "React",
      "Rust"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ishaan Verma",
    "email": "ishaan.verma@outlook.com",
    "phone": "940-839-2949",
    "ATS_score": 50,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "NoSQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Vihaan Das",
    "email": "vihaan.das@gmail.com",
    "phone": "490-383-6471",
    "ATS_score": 50,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "InnovateX",
    "skills": [
      "Vue",
      "TypeScript",
      "Docker",
      "Agile"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Saanvi Jain",
    "email": "saanvi.jain@example.com",
    "phone": "677-229-7142",
    "ATS_score": 50,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "Python",
      "NoSQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Arjun Menon",
    "email": "arjun.menon@outlook.com",
    "phone": "146-582-9396",
    "ATS_score": 50,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Data Insights",
    "skills": [
      "Machine Learning",
      "Agile"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Vivaan Das",
    "email": "vivaan.das@yahoo.com",
    "phone": "403-350-7239",
    "ATS_score": 50,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Docker"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Kavya Menon",
    "email": "kavya.menon@example.com",
    "phone": "713-265-4922",
    "ATS_score": 51,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Java",
      "HTML"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Krishna Joshi",
    "email": "krishna.joshi@example.com",
    "phone": "712-115-1882",
    "ATS_score": 51,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "Flask",
      "SQL",
      "Docker",
      "JavaScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Reyansh Das",
    "email": "reyansh.das@yahoo.com",
    "phone": "325-768-3227",
    "ATS_score": 51,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "Go",
      "React"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aditya Reddy",
    "email": "aditya.reddy@yahoo.com",
    "phone": "181-104-8205",
    "ATS_score": 51,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "Node.js",
      "DevOps"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ira Gupta",
    "email": "ira.gupta@yahoo.com",
    "phone": "739-981-8908",
    "ATS_score": 51,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Global Solutions",
    "skills": [
      "Agile",
      "Go",
      "Git"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ananya Bhat",
    "email": "ananya.bhat@outlook.com",
    "phone": "789-807-9042",
    "ATS_score": 51,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "JavaScript",
      "AWS",
      "HTML"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sai Singh",
    "email": "sai.singh@gmail.com",
    "phone": "958-411-9898",
    "ATS_score": 51,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Go",
      "Scrum",
      "AWS",
      "GraphQL",
      "React"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ishaan Bhat",
    "email": "ishaan.bhat@outlook.com",
    "phone": "106-942-6462",
    "ATS_score": 51,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Visionary Labs",
    "skills": [
      "DevOps",
      "Docker",
      "Git"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Diya Roy",
    "email": "diya.roy@outlook.com",
    "phone": "934-779-2977",
    "ATS_score": 51,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "JavaScript"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aditya Bhat",
    "email": "aditya.bhat@gmail.com",
    "phone": "558-589-5333",
    "ATS_score": 51,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Rust",
      "Docker",
      "Java",
      "Angular"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Reyansh Gupta",
    "email": "reyansh.gupta@gmail.com",
    "phone": "175-914-7090",
    "ATS_score": 52,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "DevOps",
      "AWS",
      "Data Science"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ayaan Chopra",
    "email": "ayaan.chopra@yahoo.com",
    "phone": "361-352-1664",
    "ATS_score": 52,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Node.js",
      "C#",
      "Git",
      "Django",
      "TypeScript"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Myra Mehta",
    "email": "myra.mehta@gmail.com",
    "phone": "833-637-4752",
    "ATS_score": 52,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Machine Learning",
      "CSS",
      "Kubernetes",
      "HTML"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ananya Gupta",
    "email": "ananya.gupta@gmail.com",
    "phone": "817-854-4909",
    "ATS_score": 52,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "TypeScript"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarya Chopra",
    "email": "aarya.chopra@gmail.com",
    "phone": "924-416-1542",
    "ATS_score": 52,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "NexGen",
    "skills": [
      "Angular"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Kumar",
    "email": "ayaan.kumar@example.com",
    "phone": "254-752-9664",
    "ATS_score": 52,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "Python",
      "Flask"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Roy",
    "email": "sara.roy@outlook.com",
    "phone": "611-668-3550",
    "ATS_score": 52,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "Data Insights",
    "skills": [
      "Kubernetes",
      "Go",
      "C#",
      "HTML"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Myra Joshi",
    "email": "myra.joshi@yahoo.com",
    "phone": "796-787-3238",
    "ATS_score": 52,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "Vue"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aarav Jain",
    "email": "aarav.jain@yahoo.com",
    "phone": "826-929-9678",
    "ATS_score": 52,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "SoftSys",
    "skills": [
      "Kubernetes",
      "Java",
      "Machine Learning",
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Mehta",
    "email": "avni.mehta@example.com",
    "phone": "573-243-4562",
    "ATS_score": 52,
    "yearsExperience": 6,
    "degree": "B.E Electronics",
    "previousCompany": "NexGen",
    "skills": [
      "GraphQL",
      "HTML",
      "React"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vihaan Jain",
    "email": "vihaan.jain@yahoo.com",
    "phone": "734-639-2257",
    "ATS_score": 53,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Spring"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Arjun Singh",
    "email": "arjun.singh@example.com",
    "phone": "383-611-1469",
    "ATS_score": 53,
    "yearsExperience": 6,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Visionary Labs",
    "skills": [
      "TypeScript",
      "Spring",
      "JavaScript",
      "Kubernetes",
      "Python"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarav Nair",
    "email": "aarav.nair@gmail.com",
    "phone": "973-606-6861",
    "ATS_score": 53,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Angular",
      "Data Science"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Saanvi Reddy",
    "email": "saanvi.reddy@gmail.com",
    "phone": "502-832-1914",
    "ATS_score": 53,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechWave",
    "skills": [
      "SQL",
      "Vue",
      "Rust",
      "Spring"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Sara Joshi",
    "email": "sara.joshi@yahoo.com",
    "phone": "487-510-9352",
    "ATS_score": 53,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "HTML",
      "Rust",
      "Machine Learning",
      "C#"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Arjun Singh",
    "email": "arjun.singh@gmail.com",
    "phone": "634-546-7459",
    "ATS_score": 53,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Vue",
      "Machine Learning",
      "Git"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarav Jain",
    "email": "aarav.jain@gmail.com",
    "phone": "772-893-9659",
    "ATS_score": 53,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "NexGen",
    "skills": [
      "Node.js"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Myra Kumar",
    "email": "myra.kumar@gmail.com",
    "phone": "603-924-1236",
    "ATS_score": 53,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "DataWorks",
    "skills": [
      "C#",
      "HTML",
      "TypeScript"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Kavya Verma",
    "email": "kavya.verma@gmail.com",
    "phone": "355-382-1710",
    "ATS_score": 53,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Vue",
      "Git",
      "Python",
      "Spring"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Kavya Das",
    "email": "kavya.das@yahoo.com",
    "phone": "155-997-6731",
    "ATS_score": 53,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Azure",
      "Data Science",
      "Vue",
      "TypeScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ishaan Chowdhury",
    "email": "ishaan.chowdhury@gmail.com",
    "phone": "979-368-8438",
    "ATS_score": 54,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "TechCorp",
    "skills": [
      "GraphQL",
      "Agile"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Aarav Sharma",
    "email": "aarav.sharma@example.com",
    "phone": "781-484-9438",
    "ATS_score": 54,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "C#",
      "Ruby"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ira Singh",
    "email": "ira.singh@outlook.com",
    "phone": "630-462-3637",
    "ATS_score": 54,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Spring",
      "Scrum",
      "Machine Learning"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sai Bhat",
    "email": "sai.bhat@example.com",
    "phone": "520-700-4230",
    "ATS_score": 54,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Flask"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ishaan Pillai",
    "email": "ishaan.pillai@outlook.com",
    "phone": "294-871-4174",
    "ATS_score": 54,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Java",
      "Spring",
      "TypeScript",
      "GraphQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Arjun Kumar",
    "email": "arjun.kumar@yahoo.com",
    "phone": "190-625-5788",
    "ATS_score": 54,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "SQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Project Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Iyer",
    "email": "avni.iyer@outlook.com",
    "phone": "429-499-7636",
    "ATS_score": 54,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Flask",
      "SQL",
      "Go",
      "CSS"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarya Bhat",
    "email": "aarya.bhat@example.com",
    "phone": "904-333-6272",
    "ATS_score": 54,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "CSS"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ira Bhat",
    "email": "ira.bhat@outlook.com",
    "phone": "266-911-2944",
    "ATS_score": 54,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Docker",
      "Go"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarav Verma",
    "email": "aarav.verma@example.com",
    "phone": "226-282-9087",
    "ATS_score": 54,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "DevOps",
      "Vue",
      "Python",
      "Agile",
      "Flask"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Mehta",
    "email": "avni.mehta@gmail.com",
    "phone": "351-873-8246",
    "ATS_score": 55,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "Machine Learning",
      "Python",
      "GraphQL",
      "Angular"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Krishna Sharma",
    "email": "krishna.sharma@example.com",
    "phone": "365-340-7669",
    "ATS_score": 55,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Git"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Intern"
  },
  {
    "name": "Reyansh Chopra",
    "email": "reyansh.chopra@gmail.com",
    "phone": "509-227-3085",
    "ATS_score": 55,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Java"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Reyansh Reddy",
    "email": "reyansh.reddy@example.com",
    "phone": "522-309-7160",
    "ATS_score": 55,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Scrum",
      "Django",
      "Spring",
      "Python"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Kumar",
    "email": "sara.kumar@example.com",
    "phone": "455-730-7205",
    "ATS_score": 55,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "React",
      "Scrum",
      "Machine Learning",
      "AWS"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aditya Chopra",
    "email": "aditya.chopra@outlook.com",
    "phone": "322-797-2655",
    "ATS_score": 55,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Docker",
      "Machine Learning",
      "Data Science",
      "Azure"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Avni Kapoor",
    "email": "avni.kapoor@gmail.com",
    "phone": "568-865-3485",
    "ATS_score": 55,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "CSS",
      "Flask"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aditya Gupta",
    "email": "aditya.gupta@outlook.com",
    "phone": "886-837-1826",
    "ATS_score": 55,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "JavaScript",
      "Django",
      "Git",
      "Data Science",
      "Agile"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vivaan Mehta",
    "email": "vivaan.mehta@example.com",
    "phone": "206-344-2133",
    "ATS_score": 55,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "Python",
      "Azure",
      "Git"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ishaan Bhat",
    "email": "ishaan.bhat@example.com",
    "phone": "440-300-2406",
    "ATS_score": 55,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "DevOps",
      "Ruby",
      "Rust",
      "SQL",
      "GraphQL"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Myra Kumar",
    "email": "myra.kumar@outlook.com",
    "phone": "393-666-6714",
    "ATS_score": 56,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DevSolutions",
    "skills": [
      "React",
      "CSS",
      "NoSQL",
      "Rust"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ananya Chopra",
    "email": "ananya.chopra@outlook.com",
    "phone": "172-980-6050",
    "ATS_score": 56,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "AWS",
      "React",
      "Machine Learning",
      "Django"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Game Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Arjun Kumar",
    "email": "arjun.kumar@gmail.com",
    "phone": "824-376-1882",
    "ATS_score": 56,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Flask",
      "Django"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Reyansh Gupta",
    "email": "reyansh.gupta@example.com",
    "phone": "907-743-8428",
    "ATS_score": 56,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Python",
      "Git",
      "Machine Learning",
      "Angular"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Myra Kumar",
    "email": "myra.kumar@outlook.com",
    "phone": "221-297-5436",
    "ATS_score": 56,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Angular",
      "Spring",
      "TypeScript",
      "CSS",
      "Go"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Saanvi Verma",
    "email": "saanvi.verma@gmail.com",
    "phone": "201-560-1956",
    "ATS_score": 56,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Data Science"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ayaan Jain",
    "email": "ayaan.jain@example.com",
    "phone": "754-584-3378",
    "ATS_score": 56,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "DataWorks",
    "skills": [
      "C#",
      "DevOps",
      "NoSQL",
      "Flask"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aditya Verma",
    "email": "aditya.verma@yahoo.com",
    "phone": "257-396-1188",
    "ATS_score": 56,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Rust",
      "Agile",
      "Spring",
      "Azure",
      "Git"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ayaan Mehta",
    "email": "ayaan.mehta@gmail.com",
    "phone": "440-807-2167",
    "ATS_score": 56,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Kubernetes",
      "NoSQL",
      "AWS",
      "Docker",
      "Azure"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Priya Iyer",
    "email": "priya.iyer@outlook.com",
    "phone": "279-327-1674",
    "ATS_score": 56,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "JavaScript",
      "CSS",
      "Rust",
      "Vue"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Kavya Joshi",
    "email": "kavya.joshi@outlook.com",
    "phone": "723-222-4617",
    "ATS_score": 57,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Ruby",
      "Vue",
      "Rust",
      "DevOps"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aditya Kumar",
    "email": "aditya.kumar@example.com",
    "phone": "788-635-6023",
    "ATS_score": 57,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Vue"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Menon",
    "email": "sara.menon@outlook.com",
    "phone": "352-425-6905",
    "ATS_score": 57,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Digital Solutions",
    "skills": [
      "JavaScript",
      "HTML"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Diya Verma",
    "email": "diya.verma@gmail.com",
    "phone": "386-859-1549",
    "ATS_score": 57,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Digital Solutions",
    "skills": [
      "HTML",
      "Vue",
      "Kubernetes",
      "Spring",
      "Go"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Saanvi Menon",
    "email": "saanvi.menon@gmail.com",
    "phone": "908-245-8649",
    "ATS_score": 57,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Python"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ananya Joshi",
    "email": "ananya.joshi@outlook.com",
    "phone": "437-518-3674",
    "ATS_score": 57,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Spring",
      "DevOps",
      "JavaScript",
      "Vue",
      "React"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarya Verma",
    "email": "aarya.verma@example.com",
    "phone": "327-665-8735",
    "ATS_score": 57,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Kubernetes",
      "GraphQL",
      "Go"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ayaan Reddy",
    "email": "ayaan.reddy@example.com",
    "phone": "855-704-3217",
    "ATS_score": 57,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Data Insights",
    "skills": [
      "Rust"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Kavya Menon",
    "email": "kavya.menon@example.com",
    "phone": "543-545-9688",
    "ATS_score": 57,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "GraphQL",
      "Scrum",
      "Agile",
      "Docker",
      "TypeScript"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Krishna Singh",
    "email": "krishna.singh@outlook.com",
    "phone": "760-127-2369",
    "ATS_score": 57,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Ruby"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Arjun Kumar",
    "email": "arjun.kumar@yahoo.com",
    "phone": "645-809-7143",
    "ATS_score": 58,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "Agile",
      "AWS",
      "NoSQL",
      "C#",
      "Java"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Avni Bhat",
    "email": "avni.bhat@outlook.com",
    "phone": "840-872-5270",
    "ATS_score": 58,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "Node.js",
      "Docker",
      "Django"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarav Patel",
    "email": "aarav.patel@outlook.com",
    "phone": "714-376-2021",
    "ATS_score": 58,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "Django",
      "Data Science",
      "Azure",
      "Ruby",
      "CSS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Myra Kapoor",
    "email": "myra.kapoor@gmail.com",
    "phone": "357-885-2490",
    "ATS_score": 58,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "DevOps",
      "Spring"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Kavya Nair",
    "email": "kavya.nair@yahoo.com",
    "phone": "871-670-3263",
    "ATS_score": 58,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "Spring",
      "Angular",
      "Scrum"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Vivaan Roy",
    "email": "vivaan.roy@example.com",
    "phone": "613-714-7830",
    "ATS_score": 58,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "Node.js",
      "GraphQL",
      "CSS",
      "Agile"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sai Das",
    "email": "sai.das@gmail.com",
    "phone": "551-879-7338",
    "ATS_score": 58,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Python"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Saanvi Chowdhury",
    "email": "saanvi.chowdhury@outlook.com",
    "phone": "486-924-6977",
    "ATS_score": 58,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Roy",
    "email": "ayaan.roy@yahoo.com",
    "phone": "395-231-5877",
    "ATS_score": 58,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechCorp",
    "skills": [
      "React",
      "Docker",
      "Flask"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Myra Singh",
    "email": "myra.singh@outlook.com",
    "phone": "580-233-3906",
    "ATS_score": 58,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "DevOps",
      "NoSQL",
      "CSS"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Kavya Verma",
    "email": "kavya.verma@yahoo.com",
    "phone": "375-881-4672",
    "ATS_score": 59,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Data Insights",
    "skills": [
      "Vue",
      "Python"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Avni Bhat",
    "email": "avni.bhat@example.com",
    "phone": "772-430-7568",
    "ATS_score": 59,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NexGen",
    "skills": [
      "Flask"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarya Singh",
    "email": "aarya.singh@outlook.com",
    "phone": "287-721-2712",
    "ATS_score": 59,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Kubernetes",
      "Vue",
      "Angular",
      "GraphQL",
      "SQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Vivaan Jain",
    "email": "vivaan.jain@outlook.com",
    "phone": "337-922-1389",
    "ATS_score": 59,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "DevOps",
      "Go",
      "Python",
      "GraphQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Singh",
    "email": "ayaan.singh@gmail.com",
    "phone": "716-426-3851",
    "ATS_score": 59,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "JavaScript",
      "NoSQL",
      "Node.js",
      "Azure"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sai Chopra",
    "email": "sai.chopra@example.com",
    "phone": "379-848-6285",
    "ATS_score": 59,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "DevOps",
      "Java",
      "AWS"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Sai Nair",
    "email": "sai.nair@outlook.com",
    "phone": "856-249-6700",
    "ATS_score": 59,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "C#",
      "SQL",
      "DevOps",
      "Django"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Myra Iyer",
    "email": "myra.iyer@example.com",
    "phone": "406-935-6610",
    "ATS_score": 59,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "TypeScript"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Saanvi Gupta",
    "email": "saanvi.gupta@yahoo.com",
    "phone": "433-610-6687",
    "ATS_score": 59,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Docker",
      "Vue"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Reyansh Das",
    "email": "reyansh.das@gmail.com",
    "phone": "494-634-8415",
    "ATS_score": 59,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "HTML",
      "React"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aarya Verma",
    "email": "aarya.verma@outlook.com",
    "phone": "539-818-6129",
    "ATS_score": 60,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Angular"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Sai Patel",
    "email": "sai.patel@yahoo.com",
    "phone": "288-338-4705",
    "ATS_score": 60,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Angular",
      "Git",
      "Ruby",
      "NoSQL",
      "Flask"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Priya Mehta",
    "email": "priya.mehta@gmail.com",
    "phone": "801-797-6636",
    "ATS_score": 60,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "TechCorp",
    "skills": [
      "TypeScript",
      "Kubernetes",
      "Python"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Priya Kapoor",
    "email": "priya.kapoor@outlook.com",
    "phone": "929-726-3758",
    "ATS_score": 60,
    "yearsExperience": 5,
    "degree": "B.E Electronics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Scrum",
      "Vue",
      "Spring",
      "GraphQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ayaan Chopra",
    "email": "ayaan.chopra@gmail.com",
    "phone": "608-535-8367",
    "ATS_score": 60,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Spring"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aditya Reddy",
    "email": "aditya.reddy@yahoo.com",
    "phone": "541-314-4458",
    "ATS_score": 60,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "InnovateX",
    "skills": [
      "Go",
      "Node.js",
      "Scrum",
      "Rust",
      "GraphQL"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Kavya Kapoor",
    "email": "kavya.kapoor@example.com",
    "phone": "268-344-5502",
    "ATS_score": 60,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "GraphQL",
      "AWS",
      "Git"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Diya Verma",
    "email": "diya.verma@outlook.com",
    "phone": "179-266-1707",
    "ATS_score": 60,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Angular",
      "Vue",
      "Django"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ishaan Iyer",
    "email": "ishaan.iyer@outlook.com",
    "phone": "316-612-5753",
    "ATS_score": 60,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Saanvi Sharma",
    "email": "saanvi.sharma@outlook.com",
    "phone": "714-329-9418",
    "ATS_score": 60,
    "yearsExperience": 6,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "Python",
      "SQL",
      "JavaScript",
      "Django",
      "NoSQL",
      "Agile"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Aditya Verma",
    "email": "aditya.verma@outlook.com",
    "phone": "917-399-5277",
    "ATS_score": 61,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Rust",
      "Docker",
      "Node.js",
      "NoSQL",
      "Scrum"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Kavya Jain",
    "email": "kavya.jain@example.com",
    "phone": "556-104-3574",
    "ATS_score": 61,
    "yearsExperience": 6,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "Git",
      "TypeScript",
      "DevOps"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Sai Kumar",
    "email": "sai.kumar@yahoo.com",
    "phone": "415-480-2630",
    "ATS_score": 61,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "AWS",
      "SQL",
      "Data Science",
      "HTML"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Kavya Verma",
    "email": "kavya.verma@example.com",
    "phone": "639-118-1877",
    "ATS_score": 61,
    "yearsExperience": 5,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "HTML"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Priya Chopra",
    "email": "priya.chopra@yahoo.com",
    "phone": "649-199-5808",
    "ATS_score": 61,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "NoSQL",
      "Agile",
      "Spring",
      "Django"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ishaan Chowdhury",
    "email": "ishaan.chowdhury@yahoo.com",
    "phone": "739-911-2416",
    "ATS_score": 61,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Data Insights",
    "skills": [
      "Django"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Avni Iyer",
    "email": "avni.iyer@yahoo.com",
    "phone": "505-691-6267",
    "ATS_score": 61,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "C#",
      "Java",
      "NoSQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarya Reddy",
    "email": "aarya.reddy@example.com",
    "phone": "893-418-1140",
    "ATS_score": 61,
    "yearsExperience": 6,
    "degree": "MCA",
    "previousCompany": "NexGen",
    "skills": [
      "Angular"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ira Gupta",
    "email": "ira.gupta@gmail.com",
    "phone": "434-562-5080",
    "ATS_score": 61,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Rust"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ira Joshi",
    "email": "ira.joshi@yahoo.com",
    "phone": "834-264-6791",
    "ATS_score": 61,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Spring",
      "CSS",
      "Data Science",
      "GraphQL",
      "Flask"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Myra Jain",
    "email": "myra.jain@outlook.com",
    "phone": "943-410-8730",
    "ATS_score": 62,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Rust"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Arjun Sharma",
    "email": "arjun.sharma@yahoo.com",
    "phone": "384-259-4395",
    "ATS_score": 62,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "NoSQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Kapoor",
    "email": "krishna.kapoor@yahoo.com",
    "phone": "479-936-6777",
    "ATS_score": 62,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "Digital Solutions",
    "skills": [
      "NoSQL"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ishaan Jain",
    "email": "ishaan.jain@outlook.com",
    "phone": "308-270-2033",
    "ATS_score": 62,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "DevOps"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Avni Verma",
    "email": "avni.verma@outlook.com",
    "phone": "658-351-1152",
    "ATS_score": 62,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Spring",
      "Git",
      "C#",
      "Node.js",
      "HTML",
      "Java"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aditya Kumar",
    "email": "aditya.kumar@example.com",
    "phone": "408-327-4618",
    "ATS_score": 62,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "AWS",
      "Flask",
      "Spring",
      "Node.js",
      "Scrum",
      "Rust"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Reyansh Pillai",
    "email": "reyansh.pillai@yahoo.com",
    "phone": "925-527-4618",
    "ATS_score": 62,
    "yearsExperience": 6,
    "degree": "B.E Electronics",
    "previousCompany": "Data Insights",
    "skills": [
      "Git"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarav Mehta",
    "email": "aarav.mehta@outlook.com",
    "phone": "921-311-2452",
    "ATS_score": 62,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DevSolutions",
    "skills": [
      "Kubernetes",
      "SQL",
      "Docker",
      "GraphQL",
      "Data Science"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Avni Jain",
    "email": "avni.jain@outlook.com",
    "phone": "398-909-2882",
    "ATS_score": 62,
    "yearsExperience": 6,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "SQL",
      "Machine Learning"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Krishna Kapoor",
    "email": "krishna.kapoor@example.com",
    "phone": "871-126-4715",
    "ATS_score": 62,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Angular",
      "CSS",
      "JavaScript"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Arjun Jain",
    "email": "arjun.jain@example.com",
    "phone": "513-583-8013",
    "ATS_score": 63,
    "yearsExperience": 6,
    "degree": "MCA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Ruby",
      "Git",
      "CSS",
      "AWS",
      "DevOps",
      "Rust"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ira Nair",
    "email": "ira.nair@outlook.com",
    "phone": "510-126-6437",
    "ATS_score": 63,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "DevSolutions",
    "skills": [
      "Flask"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Kavya Mehta",
    "email": "kavya.mehta@outlook.com",
    "phone": "518-300-1297",
    "ATS_score": 63,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Scrum",
      "Agile",
      "JavaScript",
      "GraphQL",
      "AWS",
      "Django"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aarav Pillai",
    "email": "aarav.pillai@gmail.com",
    "phone": "752-863-4938",
    "ATS_score": 63,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Docker",
      "Node.js"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarav Jain",
    "email": "aarav.jain@outlook.com",
    "phone": "233-851-7872",
    "ATS_score": 63,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Azure",
      "Rust",
      "TypeScript",
      "C#",
      "HTML"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Sara Roy",
    "email": "sara.roy@gmail.com",
    "phone": "150-859-2000",
    "ATS_score": 63,
    "yearsExperience": 6,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Vue",
      "Data Science",
      "Go",
      "C#",
      "SQL",
      "Python"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ira Nair",
    "email": "ira.nair@gmail.com",
    "phone": "243-260-7284",
    "ATS_score": 63,
    "yearsExperience": 6,
    "degree": "MCA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Java",
      "Rust",
      "TypeScript",
      "Machine Learning"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarya Menon",
    "email": "aarya.menon@outlook.com",
    "phone": "928-392-7037",
    "ATS_score": 63,
    "yearsExperience": 4,
    "degree": "B.E Electronics",
    "previousCompany": "Creative Minds",
    "skills": [
      "NoSQL",
      "Data Science",
      "Ruby",
      "Azure",
      "JavaScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Reyansh Pillai",
    "email": "reyansh.pillai@outlook.com",
    "phone": "328-785-9933",
    "ATS_score": 63,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Django",
      "Docker",
      "HTML",
      "Go"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ishaan Joshi",
    "email": "ishaan.joshi@yahoo.com",
    "phone": "775-877-6828",
    "ATS_score": 63,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "FutureTech",
    "skills": [
      "Docker",
      "Ruby"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aditya Chowdhury",
    "email": "aditya.chowdhury@outlook.com",
    "phone": "645-491-3411",
    "ATS_score": 64,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "TechWave",
    "skills": [
      "React",
      "HTML",
      "Node.js",
      "Azure",
      "Vue"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Arjun Bhat",
    "email": "arjun.bhat@yahoo.com",
    "phone": "492-580-7105",
    "ATS_score": 64,
    "yearsExperience": 5,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "TypeScript"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ayaan Iyer",
    "email": "ayaan.iyer@example.com",
    "phone": "762-985-3037",
    "ATS_score": 64,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Git",
      "TypeScript",
      "Machine Learning"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Vivaan Menon",
    "email": "vivaan.menon@gmail.com",
    "phone": "286-366-8857",
    "ATS_score": 64,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "HTML"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Arjun Mehta",
    "email": "arjun.mehta@gmail.com",
    "phone": "250-734-7347",
    "ATS_score": 64,
    "yearsExperience": 7,
    "degree": "B.E Electronics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Git"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ananya Iyer",
    "email": "ananya.iyer@example.com",
    "phone": "609-619-6030",
    "ATS_score": 64,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Machine Learning",
      "Azure",
      "Spring",
      "Docker",
      "Vue",
      "JavaScript"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Sai Das",
    "email": "sai.das@gmail.com",
    "phone": "670-739-5040",
    "ATS_score": 64,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "NoSQL",
      "Spring",
      "AWS",
      "Flask"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Priya Das",
    "email": "priya.das@outlook.com",
    "phone": "894-395-4022",
    "ATS_score": 64,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Data Insights",
    "skills": [
      "Git",
      "SQL",
      "Node.js",
      "Kubernetes",
      "Azure",
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Arjun Bhat",
    "email": "arjun.bhat@gmail.com",
    "phone": "872-262-9580",
    "ATS_score": 64,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "DevOps"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ishaan Roy",
    "email": "ishaan.roy@gmail.com",
    "phone": "421-789-5789",
    "ATS_score": 64,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Vue",
      "CSS",
      "Scrum",
      "Azure",
      "Machine Learning"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ananya Kapoor",
    "email": "ananya.kapoor@yahoo.com",
    "phone": "101-870-2577",
    "ATS_score": 65,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "Vue",
      "Agile"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ayaan Iyer",
    "email": "ayaan.iyer@example.com",
    "phone": "743-616-8744",
    "ATS_score": 65,
    "yearsExperience": 5,
    "degree": "B.E Electronics",
    "previousCompany": "AlphaTech",
    "skills": [
      "NoSQL",
      "Flask",
      "Azure",
      "Python",
      "Agile",
      "TypeScript"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Saanvi Iyer",
    "email": "saanvi.iyer@outlook.com",
    "phone": "367-162-9707",
    "ATS_score": 65,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "AWS"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Myra Mehta",
    "email": "myra.mehta@outlook.com",
    "phone": "585-970-9194",
    "ATS_score": 65,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Vue",
      "Data Science"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarya Jain",
    "email": "aarya.jain@example.com",
    "phone": "808-958-7717",
    "ATS_score": 65,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "SoftSys",
    "skills": [
      "Java"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ishaan Pillai",
    "email": "ishaan.pillai@gmail.com",
    "phone": "991-321-2618",
    "ATS_score": 65,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Django",
      "Java",
      "DevOps"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Sai Verma",
    "email": "sai.verma@example.com",
    "phone": "421-426-9947",
    "ATS_score": 65,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Git",
      "Ruby",
      "Azure",
      "GraphQL",
      "Kubernetes"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Priya Singh",
    "email": "priya.singh@gmail.com",
    "phone": "113-605-1557",
    "ATS_score": 65,
    "yearsExperience": 6,
    "degree": "MCA",
    "previousCompany": "TechCorp",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Kavya Chopra",
    "email": "kavya.chopra@gmail.com",
    "phone": "991-291-9845",
    "ATS_score": 65,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Ruby",
      "Python",
      "Azure",
      "CSS",
      "TypeScript",
      "Django"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Sai Roy",
    "email": "sai.roy@outlook.com",
    "phone": "890-769-1083",
    "ATS_score": 65,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "HTML"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Priya Chowdhury",
    "email": "priya.chowdhury@gmail.com",
    "phone": "631-946-9341",
    "ATS_score": 66,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "FutureTech",
    "skills": [
      "JavaScript"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Krishna Sharma",
    "email": "krishna.sharma@yahoo.com",
    "phone": "468-823-2367",
    "ATS_score": 66,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "JavaScript",
      "Rust",
      "GraphQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Krishna Iyer",
    "email": "krishna.iyer@gmail.com",
    "phone": "866-835-8034",
    "ATS_score": 66,
    "yearsExperience": 7,
    "degree": "M.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "GraphQL",
      "SQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Krishna Joshi",
    "email": "krishna.joshi@yahoo.com",
    "phone": "597-595-4342",
    "ATS_score": 66,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "TechCorp",
    "skills": [
      "NoSQL",
      "Django",
      "Java",
      "Data Science",
      "Node.js"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Priya Kapoor",
    "email": "priya.kapoor@yahoo.com",
    "phone": "323-284-6215",
    "ATS_score": 66,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Flask",
      "Java",
      "TypeScript",
      "Go",
      "Ruby",
      "Data Science"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Aarav Roy",
    "email": "aarav.roy@example.com",
    "phone": "867-596-2152",
    "ATS_score": 66,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "TypeScript",
      "JavaScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ayaan Pillai",
    "email": "ayaan.pillai@gmail.com",
    "phone": "637-323-5539",
    "ATS_score": 66,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "NoSQL",
      "DevOps",
      "Agile",
      "Spring",
      "Python"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarav Verma",
    "email": "aarav.verma@gmail.com",
    "phone": "521-198-1358",
    "ATS_score": 66,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechCorp",
    "skills": [
      "Git",
      "Go",
      "Azure"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Priya Das",
    "email": "priya.das@gmail.com",
    "phone": "650-716-5939",
    "ATS_score": 66,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Flask",
      "Go"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ishaan Iyer",
    "email": "ishaan.iyer@example.com",
    "phone": "871-826-8778",
    "ATS_score": 66,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "InnovateX",
    "skills": [
      "Agile",
      "Git",
      "Django"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Aarya Mehta",
    "email": "aarya.mehta@yahoo.com",
    "phone": "149-639-6230",
    "ATS_score": 67,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Data Insights",
    "skills": [
      "AWS",
      "TypeScript"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Avni Chopra",
    "email": "avni.chopra@outlook.com",
    "phone": "160-614-4050",
    "ATS_score": 67,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "DataWorks",
    "skills": [
      "Scrum"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aditya Nair",
    "email": "aditya.nair@gmail.com",
    "phone": "385-952-5843",
    "ATS_score": 67,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "NexGen",
    "skills": [
      "Agile",
      "TypeScript",
      "Docker",
      "CSS"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Krishna Gupta",
    "email": "krishna.gupta@example.com",
    "phone": "578-149-6287",
    "ATS_score": 67,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "React",
      "NoSQL",
      "Azure"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ayaan Gupta",
    "email": "ayaan.gupta@example.com",
    "phone": "882-847-5201",
    "ATS_score": 67,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "HTML",
      "DevOps",
      "JavaScript"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Vihaan Joshi",
    "email": "vihaan.joshi@yahoo.com",
    "phone": "547-982-8521",
    "ATS_score": 67,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "CSS",
      "C#",
      "Docker",
      "Agile",
      "Git",
      "NoSQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Myra Chowdhury",
    "email": "myra.chowdhury@outlook.com",
    "phone": "510-782-8274",
    "ATS_score": 67,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Kubernetes",
      "SQL",
      "GraphQL",
      "Docker"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Sara Iyer",
    "email": "sara.iyer@yahoo.com",
    "phone": "548-791-4617",
    "ATS_score": 67,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Docker",
      "Kubernetes",
      "TypeScript",
      "SQL",
      "HTML",
      "Python"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Krishna Mehta",
    "email": "krishna.mehta@yahoo.com",
    "phone": "223-285-8779",
    "ATS_score": 67,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "NoSQL",
      "Data Science",
      "Vue",
      "Azure"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ishaan Bhat",
    "email": "ishaan.bhat@outlook.com",
    "phone": "206-281-3428",
    "ATS_score": 67,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "NoSQL",
      "C#",
      "HTML",
      "Machine Learning",
      "TypeScript",
      "SQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Arjun Mehta",
    "email": "arjun.mehta@outlook.com",
    "phone": "690-946-2447",
    "ATS_score": 68,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "SQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Aditya Singh",
    "email": "aditya.singh@example.com",
    "phone": "616-505-4953",
    "ATS_score": 68,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "DevOps"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ishaan Mehta",
    "email": "ishaan.mehta@yahoo.com",
    "phone": "410-480-8170",
    "ATS_score": 68,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "InnovateX",
    "skills": [
      "JavaScript",
      "Azure",
      "Git",
      "HTML",
      "Machine Learning"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Vihaan Verma",
    "email": "vihaan.verma@yahoo.com",
    "phone": "647-219-2201",
    "ATS_score": 68,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "NexGen",
    "skills": [
      "Python"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Avni Kumar",
    "email": "avni.kumar@outlook.com",
    "phone": "439-192-9291",
    "ATS_score": 68,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Scrum",
      "TypeScript",
      "Data Science",
      "SQL",
      "C#"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Sai Singh",
    "email": "sai.singh@yahoo.com",
    "phone": "730-767-4246",
    "ATS_score": 68,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "TypeScript",
      "Agile",
      "React",
      "Node.js",
      "Python",
      "Go"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ira Sharma",
    "email": "ira.sharma@yahoo.com",
    "phone": "656-165-9250",
    "ATS_score": 68,
    "yearsExperience": 6,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Avni Das",
    "email": "avni.das@outlook.com",
    "phone": "494-348-8415",
    "ATS_score": 68,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "C#",
      "Git",
      "Spring",
      "TypeScript",
      "Vue",
      "NoSQL"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Diya Verma",
    "email": "diya.verma@yahoo.com",
    "phone": "215-852-4430",
    "ATS_score": 68,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Scrum",
      "AWS",
      "Spring",
      "Azure"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Reyansh Roy",
    "email": "reyansh.roy@example.com",
    "phone": "400-222-9778",
    "ATS_score": 68,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "CSS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Saanvi Gupta",
    "email": "saanvi.gupta@example.com",
    "phone": "694-996-3826",
    "ATS_score": 69,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "Creative Minds",
    "skills": [
      "React",
      "HTML",
      "Python",
      "Data Science",
      "Vue"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Gupta",
    "email": "ayaan.gupta@gmail.com",
    "phone": "423-875-3538",
    "ATS_score": 69,
    "yearsExperience": 7,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Vihaan Verma",
    "email": "vihaan.verma@outlook.com",
    "phone": "777-142-6462",
    "ATS_score": 69,
    "yearsExperience": 6,
    "degree": "MCA",
    "previousCompany": "InnovateX",
    "skills": [
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ishaan Roy",
    "email": "ishaan.roy@outlook.com",
    "phone": "497-704-8622",
    "ATS_score": 69,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "Spring"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aarya Chowdhury",
    "email": "aarya.chowdhury@example.com",
    "phone": "280-190-6047",
    "ATS_score": 69,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "CSS"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ananya Das",
    "email": "ananya.das@outlook.com",
    "phone": "759-848-4210",
    "ATS_score": 69,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "TypeScript",
      "Go",
      "Spring",
      "HTML",
      "Kubernetes"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ananya Kapoor",
    "email": "ananya.kapoor@yahoo.com",
    "phone": "259-961-3234",
    "ATS_score": 69,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Docker",
      "Kubernetes"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Avni Sharma",
    "email": "avni.sharma@yahoo.com",
    "phone": "391-443-1946",
    "ATS_score": 69,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "GraphQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Diya Kapoor",
    "email": "diya.kapoor@gmail.com",
    "phone": "706-292-7163",
    "ATS_score": 69,
    "yearsExperience": 5,
    "degree": "B.E Electronics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Machine Learning",
      "CSS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ira Pillai",
    "email": "ira.pillai@outlook.com",
    "phone": "707-904-5844",
    "ATS_score": 69,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "TypeScript",
      "Rust",
      "HTML"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ayaan Menon",
    "email": "ayaan.menon@outlook.com",
    "phone": "690-676-8110",
    "ATS_score": 70,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "CSS",
      "Go",
      "Scrum"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aarya Gupta",
    "email": "aarya.gupta@outlook.com",
    "phone": "288-148-4735",
    "ATS_score": 70,
    "yearsExperience": 7,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "Data Science"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Kumar",
    "email": "avni.kumar@example.com",
    "phone": "393-705-9305",
    "ATS_score": 70,
    "yearsExperience": 6,
    "degree": "MCA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Python",
      "Vue",
      "Flask",
      "Ruby"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Diya Das",
    "email": "diya.das@example.com",
    "phone": "667-175-2816",
    "ATS_score": 70,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "InnovateX",
    "skills": [
      "JavaScript",
      "TypeScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Aarya Sharma",
    "email": "aarya.sharma@outlook.com",
    "phone": "991-221-5493",
    "ATS_score": 70,
    "yearsExperience": 7,
    "degree": "PhD Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Java",
      "Data Science"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Diya Sharma",
    "email": "diya.sharma@example.com",
    "phone": "912-170-4347",
    "ATS_score": 70,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Spring",
      "Azure",
      "Ruby"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aditya Chowdhury",
    "email": "aditya.chowdhury@outlook.com",
    "phone": "366-569-7642",
    "ATS_score": 70,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Docker",
      "Angular"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Kapoor",
    "email": "avni.kapoor@yahoo.com",
    "phone": "506-800-4880",
    "ATS_score": 70,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Data Insights",
    "skills": [
      "TypeScript",
      "DevOps",
      "Vue",
      "C#"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aditya Roy",
    "email": "aditya.roy@outlook.com",
    "phone": "347-630-4967",
    "ATS_score": 70,
    "yearsExperience": 5,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Git",
      "Go",
      "DevOps",
      "TypeScript",
      "GraphQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ira Singh",
    "email": "ira.singh@gmail.com",
    "phone": "336-993-7322",
    "ATS_score": 70,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Data Science",
      "AWS",
      "Angular",
      "Ruby",
      "Agile",
      "Docker"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Saanvi Verma",
    "email": "saanvi.verma@gmail.com",
    "phone": "747-882-4770",
    "ATS_score": 71,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "C#",
      "Spring",
      "TypeScript",
      "Flask",
      "Ruby",
      "Node.js"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ananya Verma",
    "email": "ananya.verma@gmail.com",
    "phone": "583-525-3182",
    "ATS_score": 71,
    "yearsExperience": 7,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "GraphQL",
      "React",
      "AWS"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarya Sharma",
    "email": "aarya.sharma@example.com",
    "phone": "986-305-7370",
    "ATS_score": 71,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "Java",
      "C#",
      "Angular",
      "Agile"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Priya Menon",
    "email": "priya.menon@gmail.com",
    "phone": "274-557-4692",
    "ATS_score": 71,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "DevOps",
      "TypeScript",
      "Node.js",
      "NoSQL"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Kavya Patel",
    "email": "kavya.patel@yahoo.com",
    "phone": "383-341-4377",
    "ATS_score": 71,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "TypeScript",
      "Machine Learning",
      "Spring",
      "GraphQL",
      "Python",
      "C#"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Saanvi Nair",
    "email": "saanvi.nair@gmail.com",
    "phone": "482-853-5966",
    "ATS_score": 71,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Flask",
      "Ruby",
      "Django",
      "AWS",
      "Go",
      "CSS"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ananya Patel",
    "email": "ananya.patel@example.com",
    "phone": "319-490-7737",
    "ATS_score": 71,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Java",
      "NoSQL",
      "Flask"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Sara Singh",
    "email": "sara.singh@yahoo.com",
    "phone": "804-497-1835",
    "ATS_score": 71,
    "yearsExperience": 7,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "SQL",
      "Node.js",
      "Django",
      "Kubernetes",
      "Angular",
      "AWS",
      "Ruby"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Vivaan Pillai",
    "email": "vivaan.pillai@gmail.com",
    "phone": "411-531-2378",
    "ATS_score": 71,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "NoSQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Sai Joshi",
    "email": "sai.joshi@outlook.com",
    "phone": "192-985-6553",
    "ATS_score": 71,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Data Insights",
    "skills": [
      "Java",
      "NoSQL"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ayaan Verma",
    "email": "ayaan.verma@example.com",
    "phone": "712-705-5315",
    "ATS_score": 72,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Data Insights",
    "skills": [
      "Go",
      "Python",
      "C#"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Mehta",
    "email": "krishna.mehta@gmail.com",
    "phone": "278-534-1502",
    "ATS_score": 72,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Go",
      "Docker",
      "Spring",
      "DevOps",
      "Python",
      "JavaScript"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Arjun Pillai",
    "email": "arjun.pillai@gmail.com",
    "phone": "878-285-9405",
    "ATS_score": 72,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Global Solutions",
    "skills": [
      "Go",
      "React",
      "Spring",
      "DevOps",
      "Rust"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Sara Verma",
    "email": "sara.verma@gmail.com",
    "phone": "191-342-6607",
    "ATS_score": 72,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Flask",
      "Node.js",
      "GraphQL",
      "Kubernetes",
      "Git"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ishaan Verma",
    "email": "ishaan.verma@outlook.com",
    "phone": "417-395-1971",
    "ATS_score": 72,
    "yearsExperience": 6,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Rust",
      "Azure",
      "Flask",
      "TypeScript",
      "Python",
      "DevOps"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ananya Jain",
    "email": "ananya.jain@outlook.com",
    "phone": "311-715-2163",
    "ATS_score": 72,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "FutureTech",
    "skills": [
      "NoSQL",
      "Scrum",
      "Kubernetes",
      "Data Science",
      "Go",
      "TypeScript",
      "Git"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Myra Joshi",
    "email": "myra.joshi@yahoo.com",
    "phone": "465-228-9567",
    "ATS_score": 72,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Vue"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarav Iyer",
    "email": "aarav.iyer@example.com",
    "phone": "984-753-4242",
    "ATS_score": 72,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Java"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Reyansh Chowdhury",
    "email": "reyansh.chowdhury@yahoo.com",
    "phone": "799-667-2716",
    "ATS_score": 72,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SmartTech",
    "skills": [
      "Data Science",
      "Kubernetes",
      "Machine Learning",
      "Azure",
      "JavaScript",
      "TypeScript"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vivaan Bhat",
    "email": "vivaan.bhat@yahoo.com",
    "phone": "316-821-9120",
    "ATS_score": 72,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "Flask"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Aarya Singh",
    "email": "aarya.singh@outlook.com",
    "phone": "261-832-8240",
    "ATS_score": 73,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Flask",
      "Data Science",
      "Spring",
      "Ruby",
      "AWS"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Arjun Das",
    "email": "arjun.das@yahoo.com",
    "phone": "242-266-5290",
    "ATS_score": 73,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "TechWave",
    "skills": [
      "HTML",
      "TypeScript",
      "JavaScript"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Reyansh Mehta",
    "email": "reyansh.mehta@yahoo.com",
    "phone": "133-335-2013",
    "ATS_score": 73,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Rust",
      "Spring",
      "SQL",
      "AWS",
      "NoSQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Arjun Menon",
    "email": "arjun.menon@gmail.com",
    "phone": "274-167-4387",
    "ATS_score": 73,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Creative Minds",
    "skills": [
      "Agile",
      "HTML",
      "Java",
      "CSS",
      "Go"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vihaan Kapoor",
    "email": "vihaan.kapoor@yahoo.com",
    "phone": "932-828-1476",
    "ATS_score": 73,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "GraphQL",
      "Flask",
      "Spring",
      "Vue",
      "Data Science",
      "Machine Learning",
      "Azure"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ayaan Roy",
    "email": "ayaan.roy@outlook.com",
    "phone": "160-548-8871",
    "ATS_score": 73,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "AWS"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ananya Joshi",
    "email": "ananya.joshi@yahoo.com",
    "phone": "478-179-3606",
    "ATS_score": 73,
    "yearsExperience": 7,
    "degree": "MCA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "SQL",
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Arjun Reddy",
    "email": "arjun.reddy@outlook.com",
    "phone": "615-231-6147",
    "ATS_score": 73,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Spring",
      "Scrum"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ira Joshi",
    "email": "ira.joshi@example.com",
    "phone": "698-322-1950",
    "ATS_score": 73,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Docker",
      "Git",
      "SQL",
      "Machine Learning",
      "C#",
      "Rust",
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ayaan Bhat",
    "email": "ayaan.bhat@yahoo.com",
    "phone": "260-851-1999",
    "ATS_score": 73,
    "yearsExperience": 7,
    "degree": "MBA",
    "previousCompany": "Data Insights",
    "skills": [
      "HTML"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aditya Pillai",
    "email": "aditya.pillai@example.com",
    "phone": "713-658-2668",
    "ATS_score": 74,
    "yearsExperience": 4,
    "degree": "B.E Electronics",
    "previousCompany": "DataWorks",
    "skills": [
      "TypeScript"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sara Nair",
    "email": "sara.nair@yahoo.com",
    "phone": "860-631-4518",
    "ATS_score": 74,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "Git"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aarya Gupta",
    "email": "aarya.gupta@gmail.com",
    "phone": "746-605-5508",
    "ATS_score": 74,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Machine Learning",
      "DevOps",
      "Ruby",
      "TypeScript",
      "React"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ira Gupta",
    "email": "ira.gupta@yahoo.com",
    "phone": "560-206-9930",
    "ATS_score": 74,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SmartTech",
    "skills": [
      "C#",
      "SQL",
      "Machine Learning",
      "Ruby"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Priya Verma",
    "email": "priya.verma@yahoo.com",
    "phone": "104-802-4647",
    "ATS_score": 74,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Data Insights",
    "skills": [
      "Node.js",
      "C#",
      "GraphQL",
      "Spring",
      "Git",
      "NoSQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Diya Kumar",
    "email": "diya.kumar@gmail.com",
    "phone": "547-871-4730",
    "ATS_score": 74,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Rust",
      "Data Science",
      "Angular"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ira Chopra",
    "email": "ira.chopra@example.com",
    "phone": "843-137-7010",
    "ATS_score": 74,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "Creative Minds",
    "skills": [
      "SQL",
      "Python",
      "AWS",
      "C#",
      "Git",
      "Rust"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ira Patel",
    "email": "ira.patel@example.com",
    "phone": "674-644-8177",
    "ATS_score": 74,
    "yearsExperience": 6,
    "degree": "B.E Electronics",
    "previousCompany": "NexGen",
    "skills": [
      "Python",
      "Angular"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Project Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Arjun Mehta",
    "email": "arjun.mehta@example.com",
    "phone": "348-281-9574",
    "ATS_score": 74,
    "yearsExperience": 2,
    "degree": "MBA",
    "previousCompany": "Global Solutions",
    "skills": [
      "DevOps"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Aarya Gupta",
    "email": "aarya.gupta@yahoo.com",
    "phone": "674-540-6904",
    "ATS_score": 74,
    "yearsExperience": 5,
    "degree": "B.E Electronics",
    "previousCompany": "NexGen",
    "skills": [
      "Vue"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Reyansh Menon",
    "email": "reyansh.menon@gmail.com",
    "phone": "133-370-2571",
    "ATS_score": 75,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Python",
      "GraphQL",
      "Ruby",
      "Go",
      "Vue"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Iyer",
    "email": "avni.iyer@outlook.com",
    "phone": "663-745-7790",
    "ATS_score": 75,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "Rust",
      "Machine Learning",
      "Java",
      "Django",
      "Go"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Saanvi Roy",
    "email": "saanvi.roy@outlook.com",
    "phone": "394-741-9425",
    "ATS_score": 75,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Python"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ishaan Reddy",
    "email": "ishaan.reddy@example.com",
    "phone": "494-142-4908",
    "ATS_score": 75,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Rust",
      "Kubernetes",
      "TypeScript",
      "Angular",
      "Data Science"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Krishna Singh",
    "email": "krishna.singh@example.com",
    "phone": "251-568-9134",
    "ATS_score": 75,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "NoSQL",
      "DevOps"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Myra Singh",
    "email": "myra.singh@gmail.com",
    "phone": "822-294-6762",
    "ATS_score": 75,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Ruby",
      "Node.js",
      "Scrum"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ananya Patel",
    "email": "ananya.patel@example.com",
    "phone": "522-383-1152",
    "ATS_score": 75,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "CSS",
      "SQL",
      "Docker",
      "Rust",
      "Flask",
      "Scrum"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ishaan Chopra",
    "email": "ishaan.chopra@yahoo.com",
    "phone": "611-348-9147",
    "ATS_score": 75,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "DevOps"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Priya Das",
    "email": "priya.das@example.com",
    "phone": "102-520-7421",
    "ATS_score": 75,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "GraphQL",
      "React",
      "Scrum",
      "Machine Learning",
      "DevOps"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Vihaan Menon",
    "email": "vihaan.menon@outlook.com",
    "phone": "195-728-4723",
    "ATS_score": 75,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Spring",
      "Docker"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Vivaan Jain",
    "email": "vivaan.jain@outlook.com",
    "phone": "441-670-5938",
    "ATS_score": 76,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "JavaScript",
      "Agile",
      "Go",
      "AWS"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Singh",
    "email": "krishna.singh@gmail.com",
    "phone": "703-365-5991",
    "ATS_score": 76,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Ruby",
      "Agile",
      "Angular",
      "C#",
      "Node.js",
      "Kubernetes",
      "Docker"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ayaan Joshi",
    "email": "ayaan.joshi@yahoo.com",
    "phone": "711-992-7864",
    "ATS_score": 76,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "Node.js",
      "TypeScript",
      "DevOps",
      "Docker"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Avni Nair",
    "email": "avni.nair@example.com",
    "phone": "201-671-4343",
    "ATS_score": 76,
    "yearsExperience": 7,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "CSS",
      "Scrum",
      "JavaScript",
      "Django",
      "Angular",
      "Flask"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Sai Singh",
    "email": "sai.singh@example.com",
    "phone": "925-485-9190",
    "ATS_score": 76,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "JavaScript",
      "Ruby",
      "HTML",
      "Java",
      "Angular",
      "Docker",
      "Scrum"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ananya Reddy",
    "email": "ananya.reddy@example.com",
    "phone": "344-226-5671",
    "ATS_score": 76,
    "yearsExperience": 7,
    "degree": "B.Sc Information Technology",
    "previousCompany": "InnovateX",
    "skills": [
      "NoSQL",
      "GraphQL"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Sara Gupta",
    "email": "sara.gupta@gmail.com",
    "phone": "133-465-5579",
    "ATS_score": 76,
    "yearsExperience": 6,
    "degree": "B.Sc Mathematics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "JavaScript",
      "Django",
      "Flask",
      "Node.js",
      "Ruby"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Sara Mehta",
    "email": "sara.mehta@yahoo.com",
    "phone": "422-482-5917",
    "ATS_score": 76,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "CSS",
      "Python"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarav Reddy",
    "email": "aarav.reddy@outlook.com",
    "phone": "433-179-9243",
    "ATS_score": 76,
    "yearsExperience": 7,
    "degree": "MCA",
    "previousCompany": "DataWorks",
    "skills": [
      "Ruby",
      "Flask",
      "Docker",
      "Data Science",
      "AWS",
      "Node.js"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aditya Kumar",
    "email": "aditya.kumar@example.com",
    "phone": "547-351-4079",
    "ATS_score": 76,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "FutureTech",
    "skills": [
      "Data Science",
      "Machine Learning",
      "Rust",
      "HTML",
      "JavaScript",
      "Scrum"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ira Joshi",
    "email": "ira.joshi@outlook.com",
    "phone": "767-350-8678",
    "ATS_score": 77,
    "yearsExperience": 7,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Angular"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ishaan Singh",
    "email": "ishaan.singh@outlook.com",
    "phone": "363-464-9112",
    "ATS_score": 77,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SmartTech",
    "skills": [
      "React",
      "Data Science",
      "Flask",
      "Spring",
      "Node.js"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Intern"
  },
  {
    "name": "Aarya Chopra",
    "email": "aarya.chopra@yahoo.com",
    "phone": "539-275-5285",
    "ATS_score": 77,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Data Science"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vivaan Kapoor",
    "email": "vivaan.kapoor@example.com",
    "phone": "445-282-3847",
    "ATS_score": 77,
    "yearsExperience": 7,
    "degree": "B.E Electronics",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Scrum",
      "NoSQL",
      "C#",
      "Azure",
      "Angular",
      "Agile",
      "Flask"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Arjun Sharma",
    "email": "arjun.sharma@yahoo.com",
    "phone": "808-273-4262",
    "ATS_score": 77,
    "yearsExperience": 8,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Python",
      "Vue",
      "Azure",
      "HTML",
      "Kubernetes"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Priya Menon",
    "email": "priya.menon@example.com",
    "phone": "923-569-2375",
    "ATS_score": 77,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "React"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vihaan Kumar",
    "email": "vihaan.kumar@outlook.com",
    "phone": "319-305-5234",
    "ATS_score": 77,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Git",
      "AWS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Avni Patel",
    "email": "avni.patel@yahoo.com",
    "phone": "912-941-8140",
    "ATS_score": 77,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "Data Insights",
    "skills": [
      "Java"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aditya Gupta",
    "email": "aditya.gupta@gmail.com",
    "phone": "460-148-2497",
    "ATS_score": 77,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "NoSQL",
      "Go"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Diya Menon",
    "email": "diya.menon@yahoo.com",
    "phone": "848-120-1097",
    "ATS_score": 77,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Machine Learning",
      "Git",
      "Go",
      "NoSQL",
      "Agile",
      "Node.js",
      "Angular"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Avni Kumar",
    "email": "avni.kumar@example.com",
    "phone": "743-842-6101",
    "ATS_score": 78,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "InnovateX",
    "skills": [
      "Docker",
      "CSS",
      "DevOps",
      "Go"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Priya Gupta",
    "email": "priya.gupta@outlook.com",
    "phone": "736-798-1137",
    "ATS_score": 78,
    "yearsExperience": 7,
    "degree": "B.E Electronics",
    "previousCompany": "FutureTech",
    "skills": [
      "CSS",
      "JavaScript",
      "Python"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Aditya Chopra",
    "email": "aditya.chopra@gmail.com",
    "phone": "280-198-1974",
    "ATS_score": 78,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "NexGen",
    "skills": [
      "Scrum",
      "Git"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Arjun Verma",
    "email": "arjun.verma@yahoo.com",
    "phone": "596-517-4199",
    "ATS_score": 78,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "TypeScript",
      "Kubernetes",
      "GraphQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Diya Das",
    "email": "diya.das@gmail.com",
    "phone": "495-954-6002",
    "ATS_score": 78,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "Creative Minds",
    "skills": [
      "Go",
      "Scrum",
      "JavaScript",
      "SQL",
      "CSS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ira Singh",
    "email": "ira.singh@example.com",
    "phone": "476-287-5766",
    "ATS_score": 78,
    "yearsExperience": 7,
    "degree": "MBA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "React",
      "Vue"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarav Kapoor",
    "email": "aarav.kapoor@yahoo.com",
    "phone": "569-352-8485",
    "ATS_score": 78,
    "yearsExperience": 6,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "JavaScript",
      "Vue",
      "Git",
      "TypeScript",
      "Docker",
      "Ruby"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ira Gupta",
    "email": "ira.gupta@outlook.com",
    "phone": "671-299-7941",
    "ATS_score": 78,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Flask",
      "Vue",
      "Node.js"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aarav Sharma",
    "email": "aarav.sharma@outlook.com",
    "phone": "569-752-8862",
    "ATS_score": 78,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "DataWorks",
    "skills": [
      "Agile"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vihaan Verma",
    "email": "vihaan.verma@yahoo.com",
    "phone": "846-124-9195",
    "ATS_score": 78,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Data Science",
      "Ruby",
      "Angular",
      "TypeScript",
      "Node.js",
      "Rust",
      "Go"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sara Kumar",
    "email": "sara.kumar@example.com",
    "phone": "128-109-8423",
    "ATS_score": 79,
    "yearsExperience": 8,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "Rust",
      "Spring",
      "C#",
      "Machine Learning",
      "Flask",
      "DevOps",
      "NoSQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Ira Roy",
    "email": "ira.roy@example.com",
    "phone": "106-459-3793",
    "ATS_score": 79,
    "yearsExperience": 8,
    "degree": "B.E Electronics",
    "previousCompany": "Data Insights",
    "skills": [
      "Git",
      "Spring",
      "Node.js"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sai Chopra",
    "email": "sai.chopra@yahoo.com",
    "phone": "356-763-8196",
    "ATS_score": 79,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "GraphQL",
      "CSS",
      "Machine Learning",
      "Django",
      "Git",
      "Agile",
      "Scrum"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Diya Sharma",
    "email": "diya.sharma@gmail.com",
    "phone": "737-727-2691",
    "ATS_score": 79,
    "yearsExperience": 8,
    "degree": "MBA",
    "previousCompany": "Visionary Labs",
    "skills": [
      "AWS",
      "TypeScript",
      "Node.js"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Aarya Bhat",
    "email": "aarya.bhat@yahoo.com",
    "phone": "649-452-6431",
    "ATS_score": 79,
    "yearsExperience": 5,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "Go",
      "Docker"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Krishna Iyer",
    "email": "krishna.iyer@outlook.com",
    "phone": "629-679-1689",
    "ATS_score": 79,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "DevOps",
      "Data Science",
      "Rust",
      "Ruby",
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Krishna Reddy",
    "email": "krishna.reddy@gmail.com",
    "phone": "970-358-3946",
    "ATS_score": 79,
    "yearsExperience": 1,
    "degree": "M.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Flask"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Priya Verma",
    "email": "priya.verma@gmail.com",
    "phone": "972-670-1144",
    "ATS_score": 79,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Angular",
      "Data Science",
      "NoSQL",
      "React",
      "AWS"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@gmail.com",
    "phone": "332-982-6891",
    "ATS_score": 79,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "Data Insights",
    "skills": [
      "Agile",
      "Go",
      "Git",
      "GraphQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aarya Patel",
    "email": "aarya.patel@outlook.com",
    "phone": "137-780-2628",
    "ATS_score": 79,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "Creative Minds",
    "skills": [
      "CSS",
      "Machine Learning",
      "Spring",
      "JavaScript"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarya Gupta",
    "email": "aarya.gupta@gmail.com",
    "phone": "660-206-9688",
    "ATS_score": 80,
    "yearsExperience": 8,
    "degree": "B.E Electronics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Django",
      "Spring",
      "Go"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Priya Sharma",
    "email": "priya.sharma@yahoo.com",
    "phone": "580-686-5604",
    "ATS_score": 80,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "NoSQL",
      "DevOps",
      "Node.js"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Reyansh Roy",
    "email": "reyansh.roy@outlook.com",
    "phone": "665-941-4761",
    "ATS_score": 80,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Flask",
      "CSS",
      "Go",
      "Scrum",
      "SQL",
      "Rust",
      "Spring"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Sara Singh",
    "email": "sara.singh@outlook.com",
    "phone": "427-344-1263",
    "ATS_score": 80,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "FutureTech",
    "skills": [
      "Python",
      "JavaScript",
      "Angular",
      "CSS",
      "C#"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Myra Pillai",
    "email": "myra.pillai@example.com",
    "phone": "518-268-3129",
    "ATS_score": 80,
    "yearsExperience": 8,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "JavaScript",
      "React",
      "Docker"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@example.com",
    "phone": "657-541-2871",
    "ATS_score": 80,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "TechCorp",
    "skills": [
      "Java",
      "DevOps",
      "Node.js",
      "Django"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Aarav Das",
    "email": "aarav.das@example.com",
    "phone": "477-872-3097",
    "ATS_score": 80,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "Spring",
      "TypeScript",
      "Agile",
      "DevOps",
      "JavaScript",
      "Vue"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Saanvi Pillai",
    "email": "saanvi.pillai@gmail.com",
    "phone": "938-474-7816",
    "ATS_score": 80,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Flask",
      "CSS"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Avni Gupta",
    "email": "avni.gupta@example.com",
    "phone": "507-728-3429",
    "ATS_score": 80,
    "yearsExperience": 8,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Go"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Vihaan Nair",
    "email": "vihaan.nair@outlook.com",
    "phone": "536-702-1941",
    "ATS_score": 80,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "SQL",
      "Node.js",
      "Data Science",
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aarav Pillai",
    "email": "aarav.pillai@yahoo.com",
    "phone": "524-108-6969",
    "ATS_score": 81,
    "yearsExperience": 7,
    "degree": "B.Tech Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "NoSQL",
      "Kubernetes",
      "Go",
      "JavaScript",
      "Ruby"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Vivaan Patel",
    "email": "vivaan.patel@gmail.com",
    "phone": "563-322-7578",
    "ATS_score": 81,
    "yearsExperience": 8,
    "degree": "MCA",
    "previousCompany": "SmartTech",
    "skills": [
      "C#",
      "Machine Learning",
      "JavaScript",
      "Python",
      "Django",
      "Node.js",
      "Spring"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Aditya Gupta",
    "email": "aditya.gupta@outlook.com",
    "phone": "587-967-9332",
    "ATS_score": 81,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "Machine Learning",
      "Docker",
      "Azure",
      "NoSQL",
      "AWS",
      "Python",
      "Data Science"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@example.com",
    "phone": "887-228-2000",
    "ATS_score": 81,
    "yearsExperience": 7,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Avni Kumar",
    "email": "avni.kumar@gmail.com",
    "phone": "162-959-7088",
    "ATS_score": 81,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "AWS",
      "Node.js",
      "Azure",
      "React",
      "Django",
      "DevOps",
      "CSS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Aarav Jain",
    "email": "aarav.jain@outlook.com",
    "phone": "972-783-6575",
    "ATS_score": 81,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "Rust",
      "Angular"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Krishna Jain",
    "email": "krishna.jain@gmail.com",
    "phone": "462-538-6153",
    "ATS_score": 81,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "TechWave",
    "skills": [
      "Data Science",
      "Java",
      "Git",
      "Rust"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Vihaan Jain",
    "email": "vihaan.jain@example.com",
    "phone": "263-451-6696",
    "ATS_score": 81,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "DevSolutions",
    "skills": [
      "Docker"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Myra Pillai",
    "email": "myra.pillai@gmail.com",
    "phone": "155-972-9828",
    "ATS_score": 81,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "NoSQL",
      "Kubernetes",
      "JavaScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ananya Mehta",
    "email": "ananya.mehta@gmail.com",
    "phone": "755-750-1193",
    "ATS_score": 81,
    "yearsExperience": 7,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Azure",
      "NoSQL",
      "Angular",
      "Flask",
      "JavaScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ira Chowdhury",
    "email": "ira.chowdhury@gmail.com",
    "phone": "996-545-5541",
    "ATS_score": 82,
    "yearsExperience": 7,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "Azure"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ayaan Iyer",
    "email": "ayaan.iyer@gmail.com",
    "phone": "574-507-2403",
    "ATS_score": 82,
    "yearsExperience": 8,
    "degree": "MCA",
    "previousCompany": "TechCorp",
    "skills": [
      "Angular",
      "Go",
      "Data Science",
      "Python"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Sai Nair",
    "email": "sai.nair@gmail.com",
    "phone": "648-452-3406",
    "ATS_score": 82,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Machine Learning",
      "Git",
      "Python"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Product Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sara Roy",
    "email": "sara.roy@yahoo.com",
    "phone": "637-257-3266",
    "ATS_score": 82,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Machine Learning",
      "Go",
      "Data Science",
      "Scrum",
      "GraphQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sara Das",
    "email": "sara.das@outlook.com",
    "phone": "273-368-1002",
    "ATS_score": 82,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "CSS",
      "Angular",
      "AWS",
      "JavaScript",
      "Vue",
      "GraphQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Verma",
    "email": "ayaan.verma@outlook.com",
    "phone": "570-405-7635",
    "ATS_score": 82,
    "yearsExperience": 0,
    "degree": "B.E Electronics",
    "previousCompany": "NexGen",
    "skills": [
      "Node.js"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Aarav Iyer",
    "email": "aarav.iyer@outlook.com",
    "phone": "381-868-9120",
    "ATS_score": 82,
    "yearsExperience": 7,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Machine Learning"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Kavya Singh",
    "email": "kavya.singh@example.com",
    "phone": "130-261-3447",
    "ATS_score": 82,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "HTML",
      "SQL"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Arjun Kapoor",
    "email": "arjun.kapoor@gmail.com",
    "phone": "842-224-2730",
    "ATS_score": 82,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "CSS"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ananya Nair",
    "email": "ananya.nair@example.com",
    "phone": "462-244-2974",
    "ATS_score": 82,
    "yearsExperience": 8,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "Data Science",
      "CSS"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vihaan Iyer",
    "email": "vihaan.iyer@example.com",
    "phone": "689-791-5776",
    "ATS_score": 83,
    "yearsExperience": 7,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Saanvi Nair",
    "email": "saanvi.nair@example.com",
    "phone": "167-662-4145",
    "ATS_score": 83,
    "yearsExperience": 3,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "Spring",
      "JavaScript",
      "DevOps"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Reyansh Bhat",
    "email": "reyansh.bhat@outlook.com",
    "phone": "641-457-3017",
    "ATS_score": 83,
    "yearsExperience": 8,
    "degree": "MCA",
    "previousCompany": "FutureTech",
    "skills": [
      "GraphQL",
      "Angular",
      "JavaScript"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Priya Kumar",
    "email": "priya.kumar@yahoo.com",
    "phone": "446-892-8983",
    "ATS_score": 83,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "GraphQL",
      "Node.js",
      "Flask",
      "Spring",
      "Docker"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Vivaan Verma",
    "email": "vivaan.verma@outlook.com",
    "phone": "507-155-3262",
    "ATS_score": 83,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Scrum",
      "Git",
      "Machine Learning",
      "Go",
      "Agile",
      "Angular",
      "NoSQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Kavya Roy",
    "email": "kavya.roy@example.com",
    "phone": "905-296-2821",
    "ATS_score": 83,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Creative Minds",
    "skills": [
      "DevOps",
      "C#",
      "GraphQL",
      "Angular",
      "Django"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Sai Pillai",
    "email": "sai.pillai@gmail.com",
    "phone": "118-710-4535",
    "ATS_score": 83,
    "yearsExperience": 5,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Angular",
      "C#",
      "Rust",
      "Spring",
      "Django",
      "GraphQL",
      "Vue"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Sai Chopra",
    "email": "sai.chopra@example.com",
    "phone": "782-410-7721",
    "ATS_score": 83,
    "yearsExperience": 4,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Data Science",
      "Agile",
      "Flask",
      "Machine Learning"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Priya Verma",
    "email": "priya.verma@gmail.com",
    "phone": "386-362-8800",
    "ATS_score": 83,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "Azure",
      "Flask",
      "Data Science",
      "Angular"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ananya Jain",
    "email": "ananya.jain@example.com",
    "phone": "966-585-7636",
    "ATS_score": 83,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Docker",
      "TypeScript",
      "Rust",
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Arjun Mehta",
    "email": "arjun.mehta@gmail.com",
    "phone": "791-264-1197",
    "ATS_score": 84,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Scrum"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Ananya Sharma",
    "email": "ananya.sharma@gmail.com",
    "phone": "584-717-1903",
    "ATS_score": 84,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "JavaScript",
      "Django",
      "AWS",
      "Machine Learning",
      "Spring",
      "Docker",
      "React"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@example.com",
    "phone": "184-270-4819",
    "ATS_score": 84,
    "yearsExperience": 7,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "React",
      "TypeScript",
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aarav Reddy",
    "email": "aarav.reddy@gmail.com",
    "phone": "208-612-9953",
    "ATS_score": 84,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Node.js",
      "Angular",
      "Ruby",
      "Git",
      "Go",
      "Docker",
      "DevOps"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vivaan Kapoor",
    "email": "vivaan.kapoor@yahoo.com",
    "phone": "101-179-4688",
    "ATS_score": 84,
    "yearsExperience": 7,
    "degree": "B.E Electronics",
    "previousCompany": "Global Solutions",
    "skills": [
      "Machine Learning",
      "Git",
      "SQL",
      "AWS",
      "Rust",
      "JavaScript",
      "C#"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Aarya Jain",
    "email": "aarya.jain@gmail.com",
    "phone": "168-352-7194",
    "ATS_score": 84,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DevSolutions",
    "skills": [
      "Angular",
      "JavaScript",
      "CSS",
      "Spring",
      "GraphQL",
      "Agile"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Sai Iyer",
    "email": "sai.iyer@yahoo.com",
    "phone": "776-839-5527",
    "ATS_score": 84,
    "yearsExperience": 9,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Ruby"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Avni Jain",
    "email": "avni.jain@yahoo.com",
    "phone": "329-513-3903",
    "ATS_score": 84,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SoftSys",
    "skills": [
      "Machine Learning",
      "DevOps",
      "Rust",
      "Azure",
      "TypeScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Myra Singh",
    "email": "myra.singh@outlook.com",
    "phone": "845-978-9514",
    "ATS_score": 84,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Agile",
      "Angular"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Sara Verma",
    "email": "sara.verma@outlook.com",
    "phone": "188-698-9419",
    "ATS_score": 84,
    "yearsExperience": 7,
    "degree": "B.Sc Information Technology",
    "previousCompany": "FutureTech",
    "skills": [
      "Git",
      "TypeScript",
      "Python",
      "C#",
      "Ruby",
      "Data Science",
      "Spring"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Arjun Joshi",
    "email": "arjun.joshi@yahoo.com",
    "phone": "519-446-1903",
    "ATS_score": 85,
    "yearsExperience": 7,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "JavaScript",
      "Spring",
      "Ruby",
      "AWS",
      "CSS",
      "SQL"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Vivaan Bhat",
    "email": "vivaan.bhat@example.com",
    "phone": "797-656-5691",
    "ATS_score": 85,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Node.js"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Reyansh Nair",
    "email": "reyansh.nair@example.com",
    "phone": "310-565-1876",
    "ATS_score": 85,
    "yearsExperience": 8,
    "degree": "PhD Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Java"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ananya Joshi",
    "email": "ananya.joshi@yahoo.com",
    "phone": "328-283-2030",
    "ATS_score": 85,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "GraphQL",
      "JavaScript",
      "Rust"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Sara Kumar",
    "email": "sara.kumar@outlook.com",
    "phone": "446-171-4139",
    "ATS_score": 85,
    "yearsExperience": 8,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Kubernetes",
      "Scrum",
      "Node.js",
      "Docker",
      "Angular",
      "Azure",
      "Machine Learning"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Saanvi Singh",
    "email": "saanvi.singh@yahoo.com",
    "phone": "379-279-2693",
    "ATS_score": 85,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "GraphQL",
      "NoSQL",
      "TypeScript",
      "Node.js",
      "Scrum",
      "SQL",
      "React"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Myra Iyer",
    "email": "myra.iyer@gmail.com",
    "phone": "421-637-5386",
    "ATS_score": 85,
    "yearsExperience": 4,
    "degree": "PhD Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Angular"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Aarav Chowdhury",
    "email": "aarav.chowdhury@example.com",
    "phone": "646-302-2699",
    "ATS_score": 85,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Java",
      "Scrum",
      "GraphQL",
      "Spring",
      "Rust",
      "Python"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Avni Bhat",
    "email": "avni.bhat@example.com",
    "phone": "764-117-3753",
    "ATS_score": 85,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "SQL",
      "Docker",
      "NoSQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Diya Patel",
    "email": "diya.patel@example.com",
    "phone": "134-303-5346",
    "ATS_score": 85,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Angular",
      "GraphQL",
      "Python",
      "TypeScript",
      "HTML",
      "Flask",
      "Ruby"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Reyansh Mehta",
    "email": "reyansh.mehta@outlook.com",
    "phone": "652-198-5373",
    "ATS_score": 86,
    "yearsExperience": 9,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "Azure"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Arjun Sharma",
    "email": "arjun.sharma@outlook.com",
    "phone": "877-503-8348",
    "ATS_score": 86,
    "yearsExperience": 9,
    "degree": "B.E Electronics",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Scrum",
      "Azure",
      "Git",
      "TypeScript",
      "React",
      "DevOps",
      "Angular"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Sara Jain",
    "email": "sara.jain@yahoo.com",
    "phone": "347-805-3401",
    "ATS_score": 86,
    "yearsExperience": 7,
    "degree": "MCA",
    "previousCompany": "SmartTech",
    "skills": [
      "Rust",
      "Docker",
      "Agile"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Sara Verma",
    "email": "sara.verma@gmail.com",
    "phone": "579-320-4732",
    "ATS_score": 86,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Global Solutions",
    "skills": [
      "TypeScript",
      "Flask",
      "Django",
      "Agile",
      "DevOps",
      "Azure"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarav Chowdhury",
    "email": "aarav.chowdhury@example.com",
    "phone": "329-205-5297",
    "ATS_score": 86,
    "yearsExperience": 1,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechWave",
    "skills": [
      "Django",
      "HTML",
      "C#",
      "Machine Learning",
      "Spring",
      "JavaScript",
      "AWS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Saanvi Das",
    "email": "saanvi.das@outlook.com",
    "phone": "736-466-1324",
    "ATS_score": 86,
    "yearsExperience": 8,
    "degree": "MBA",
    "previousCompany": "FutureTech",
    "skills": [
      "HTML"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Vivaan Singh",
    "email": "vivaan.singh@outlook.com",
    "phone": "399-797-9458",
    "ATS_score": 86,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "TypeScript",
      "SQL",
      "HTML",
      "Vue",
      "DevOps"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Myra Jain",
    "email": "myra.jain@example.com",
    "phone": "684-874-7509",
    "ATS_score": 86,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Java",
      "HTML",
      "Flask"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Reddy",
    "email": "avni.reddy@gmail.com",
    "phone": "361-408-3819",
    "ATS_score": 86,
    "yearsExperience": 5,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "DevOps",
      "AWS",
      "Spring"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Kavya Das",
    "email": "kavya.das@outlook.com",
    "phone": "403-735-4153",
    "ATS_score": 86,
    "yearsExperience": 8,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Docker",
      "Django",
      "Python",
      "Kubernetes",
      "Scrum",
      "Java"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ayaan Nair",
    "email": "ayaan.nair@example.com",
    "phone": "259-594-1625",
    "ATS_score": 87,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Kubernetes",
      "JavaScript",
      "Scrum",
      "Java",
      "Node.js",
      "AWS",
      "Git"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Krishna Kapoor",
    "email": "krishna.kapoor@example.com",
    "phone": "724-222-3546",
    "ATS_score": 87,
    "yearsExperience": 8,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SmartTech",
    "skills": [
      "HTML"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Kavya Kumar",
    "email": "kavya.kumar@yahoo.com",
    "phone": "770-115-6083",
    "ATS_score": 87,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "CSS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vihaan Kumar",
    "email": "vihaan.kumar@gmail.com",
    "phone": "301-390-4123",
    "ATS_score": 87,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "Scrum",
      "Django",
      "SQL",
      "Node.js",
      "Kubernetes",
      "Agile"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Intern"
  },
  {
    "name": "Avni Singh",
    "email": "avni.singh@gmail.com",
    "phone": "468-254-3119",
    "ATS_score": 87,
    "yearsExperience": 7,
    "degree": "B.Sc Mathematics",
    "previousCompany": "AlphaTech",
    "skills": [
      "Scrum",
      "Go",
      "TypeScript"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Diya Singh",
    "email": "diya.singh@example.com",
    "phone": "965-980-9197",
    "ATS_score": 87,
    "yearsExperience": 6,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Data Insights",
    "skills": [
      "DevOps",
      "Flask",
      "Agile",
      "AWS",
      "Django",
      "JavaScript"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Vivaan Gupta",
    "email": "vivaan.gupta@example.com",
    "phone": "143-374-1696",
    "ATS_score": 87,
    "yearsExperience": 6,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Machine Learning",
      "Docker"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@yahoo.com",
    "phone": "317-810-7193",
    "ATS_score": 87,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "InnovateX",
    "skills": [
      "NoSQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Vivaan Roy",
    "email": "vivaan.roy@example.com",
    "phone": "453-783-7644",
    "ATS_score": 87,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "InnovateX",
    "skills": [
      "AWS",
      "TypeScript",
      "HTML",
      "Rust"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Myra Sharma",
    "email": "myra.sharma@example.com",
    "phone": "542-887-2314",
    "ATS_score": 87,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "Rust",
      "Angular",
      "Node.js",
      "GraphQL",
      "Java",
      "Go",
      "React"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vihaan Kapoor",
    "email": "vihaan.kapoor@example.com",
    "phone": "105-299-7039",
    "ATS_score": 88,
    "yearsExperience": 8,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Go",
      "C#",
      "NoSQL",
      "Rust"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ayaan Pillai",
    "email": "ayaan.pillai@example.com",
    "phone": "507-825-8696",
    "ATS_score": 88,
    "yearsExperience": 9,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "Angular",
      "AWS",
      "Flask",
      "Scrum",
      "DevOps"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Diya Jain",
    "email": "diya.jain@outlook.com",
    "phone": "569-619-4831",
    "ATS_score": 88,
    "yearsExperience": 7,
    "degree": "B.E Electronics",
    "previousCompany": "DevSolutions",
    "skills": [
      "Git",
      "GraphQL",
      "Data Science"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Saanvi Nair",
    "email": "saanvi.nair@yahoo.com",
    "phone": "783-973-2458",
    "ATS_score": 88,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "CSS",
      "Git",
      "Data Science",
      "Kubernetes",
      "Go"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ananya Kapoor",
    "email": "ananya.kapoor@outlook.com",
    "phone": "265-859-7459",
    "ATS_score": 88,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "Ruby",
      "Django",
      "Rust"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarya Reddy",
    "email": "aarya.reddy@outlook.com",
    "phone": "450-271-3981",
    "ATS_score": 88,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "JavaScript",
      "Data Science"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ira Iyer",
    "email": "ira.iyer@example.com",
    "phone": "636-351-5650",
    "ATS_score": 88,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "NoSQL"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Kavya Kumar",
    "email": "kavya.kumar@example.com",
    "phone": "368-661-7517",
    "ATS_score": 88,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "NoSQL",
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Saanvi Chopra",
    "email": "saanvi.chopra@gmail.com",
    "phone": "109-706-7536",
    "ATS_score": 88,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "GraphQL",
      "SQL",
      "HTML",
      "Agile",
      "Kubernetes"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Priya Bhat",
    "email": "priya.bhat@outlook.com",
    "phone": "726-681-4258",
    "ATS_score": 88,
    "yearsExperience": 9,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechCorp",
    "skills": [
      "GraphQL",
      "Python",
      "SQL",
      "Node.js",
      "Angular",
      "Ruby"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Reyansh Das",
    "email": "reyansh.das@yahoo.com",
    "phone": "427-374-6550",
    "ATS_score": 89,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Machine Learning",
      "Scrum"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ira Reddy",
    "email": "ira.reddy@example.com",
    "phone": "621-597-8150",
    "ATS_score": 89,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "React"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ayaan Verma",
    "email": "ayaan.verma@outlook.com",
    "phone": "963-103-7490",
    "ATS_score": 89,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Agile",
      "Angular",
      "DevOps",
      "Data Science"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Vihaan Kapoor",
    "email": "vihaan.kapoor@outlook.com",
    "phone": "542-269-5436",
    "ATS_score": 89,
    "yearsExperience": 7,
    "degree": "B.Tech Computer Science",
    "previousCompany": "Global Solutions",
    "skills": [
      "Angular",
      "DevOps",
      "Java",
      "NoSQL",
      "JavaScript",
      "Python"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Sara Kumar",
    "email": "sara.kumar@example.com",
    "phone": "594-340-9052",
    "ATS_score": 89,
    "yearsExperience": 2,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "DevOps",
      "Agile"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aditya Roy",
    "email": "aditya.roy@outlook.com",
    "phone": "822-163-6303",
    "ATS_score": 89,
    "yearsExperience": 9,
    "degree": "M.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "DevOps"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Vivaan Bhat",
    "email": "vivaan.bhat@yahoo.com",
    "phone": "246-583-4325",
    "ATS_score": 89,
    "yearsExperience": 6,
    "degree": "MCA",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Node.js",
      "Spring",
      "Django",
      "Machine Learning",
      "Python",
      "AWS"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Priya Pillai",
    "email": "priya.pillai@outlook.com",
    "phone": "482-323-5448",
    "ATS_score": 89,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Python",
      "HTML",
      "React",
      "Scrum",
      "NoSQL",
      "Rust"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Vihaan Chopra",
    "email": "vihaan.chopra@yahoo.com",
    "phone": "576-956-6201",
    "ATS_score": 89,
    "yearsExperience": 8,
    "degree": "MCA",
    "previousCompany": "SoftSys",
    "skills": [
      "Scrum"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ira Bhat",
    "email": "ira.bhat@gmail.com",
    "phone": "348-125-9505",
    "ATS_score": 89,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Rust"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Sai Chopra",
    "email": "sai.chopra@yahoo.com",
    "phone": "913-829-4360",
    "ATS_score": 90,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "SQL",
      "Machine Learning",
      "C#",
      "Rust",
      "Node.js",
      "Flask",
      "DevOps"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Vivaan Sharma",
    "email": "vivaan.sharma@yahoo.com",
    "phone": "887-156-3100",
    "ATS_score": 90,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Scrum",
      "AWS"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Krishna Kapoor",
    "email": "krishna.kapoor@example.com",
    "phone": "383-609-4225",
    "ATS_score": 90,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "React",
      "SQL",
      "Scrum",
      "Go",
      "Django"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Jain",
    "email": "avni.jain@gmail.com",
    "phone": "235-373-9721",
    "ATS_score": 90,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Django"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Ira Mehta",
    "email": "ira.mehta@outlook.com",
    "phone": "405-895-7099",
    "ATS_score": 90,
    "yearsExperience": 8,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "CSS",
      "NoSQL",
      "Machine Learning",
      "Python"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ananya Reddy",
    "email": "ananya.reddy@outlook.com",
    "phone": "623-369-9865",
    "ATS_score": 90,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Node.js"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarya Bhat",
    "email": "aarya.bhat@example.com",
    "phone": "922-867-1094",
    "ATS_score": 90,
    "yearsExperience": 3,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "SQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aarav Kapoor",
    "email": "aarav.kapoor@example.com",
    "phone": "368-583-8322",
    "ATS_score": 90,
    "yearsExperience": 7,
    "degree": "MBA",
    "previousCompany": "TechWave",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ayaan Joshi",
    "email": "ayaan.joshi@outlook.com",
    "phone": "584-449-2965",
    "ATS_score": 90,
    "yearsExperience": 1,
    "degree": "MCA",
    "previousCompany": "DataWorks",
    "skills": [
      "DevOps",
      "CSS",
      "AWS",
      "Spring"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Intern"
  },
  {
    "name": "Kavya Patel",
    "email": "kavya.patel@gmail.com",
    "phone": "108-825-4451",
    "ATS_score": 90,
    "yearsExperience": 5,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Data Insights",
    "skills": [
      "CSS",
      "DevOps",
      "Node.js",
      "Angular",
      "Azure",
      "Vue",
      "Ruby"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Aditya Chowdhury",
    "email": "aditya.chowdhury@gmail.com",
    "phone": "930-722-6041",
    "ATS_score": 91,
    "yearsExperience": 0,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "C#",
      "Spring",
      "AWS",
      "HTML"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Myra Chopra",
    "email": "myra.chopra@example.com",
    "phone": "382-118-5708",
    "ATS_score": 91,
    "yearsExperience": 0,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "CSS",
      "Node.js",
      "GraphQL",
      "Docker",
      "Rust",
      "Ruby"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Reyansh Reddy",
    "email": "reyansh.reddy@yahoo.com",
    "phone": "620-634-7217",
    "ATS_score": 91,
    "yearsExperience": 8,
    "degree": "B.Sc Information Technology",
    "previousCompany": "CodeCrafters",
    "skills": [
      "AWS",
      "Azure",
      "Data Science",
      "Docker",
      "Angular",
      "Vue",
      "Flask"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Vivaan Pillai",
    "email": "vivaan.pillai@example.com",
    "phone": "355-477-8795",
    "ATS_score": 91,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "SQL",
      "Kubernetes",
      "Scrum",
      "Spring",
      "Python",
      "Machine Learning"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aarav Menon",
    "email": "aarav.menon@yahoo.com",
    "phone": "710-624-2703",
    "ATS_score": 91,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "TechWave",
    "skills": [
      "React",
      "DevOps",
      "Python"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Diya Mehta",
    "email": "diya.mehta@example.com",
    "phone": "449-219-8918",
    "ATS_score": 91,
    "yearsExperience": 2,
    "degree": "PhD Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Machine Learning",
      "NoSQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ishaan Sharma",
    "email": "ishaan.sharma@yahoo.com",
    "phone": "105-794-1007",
    "ATS_score": 91,
    "yearsExperience": 0,
    "degree": "MCA",
    "previousCompany": "AlphaTech",
    "skills": [
      "Python",
      "React",
      "Scrum",
      "Git"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Bhat",
    "email": "sara.bhat@gmail.com",
    "phone": "580-921-7282",
    "ATS_score": 91,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Data Science",
      "SQL"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Arjun Jain",
    "email": "arjun.jain@outlook.com",
    "phone": "837-208-8822",
    "ATS_score": 91,
    "yearsExperience": 2,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "Angular",
      "Go",
      "Machine Learning",
      "AWS",
      "Docker"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarya Singh",
    "email": "aarya.singh@example.com",
    "phone": "933-297-7416",
    "ATS_score": 91,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "C#",
      "Django",
      "DevOps",
      "HTML",
      "Go"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ananya Menon",
    "email": "ananya.menon@gmail.com",
    "phone": "868-597-3707",
    "ATS_score": 92,
    "yearsExperience": 7,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "Azure",
      "Scrum",
      "NoSQL",
      "Python",
      "Rust",
      "SQL"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Saanvi Verma",
    "email": "saanvi.verma@example.com",
    "phone": "401-263-2886",
    "ATS_score": 92,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Kavya Bhat",
    "email": "kavya.bhat@outlook.com",
    "phone": "972-617-4565",
    "ATS_score": 92,
    "yearsExperience": 5,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Vue",
      "Git",
      "Flask",
      "Rust",
      "Ruby",
      "C#",
      "GraphQL"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "IT Support Specialist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Arjun Patel",
    "email": "arjun.patel@example.com",
    "phone": "455-394-5747",
    "ATS_score": 92,
    "yearsExperience": 9,
    "degree": "B.E Electronics",
    "previousCompany": "Data Insights",
    "skills": [
      "React",
      "C#",
      "NoSQL"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Reyansh Roy",
    "email": "reyansh.roy@gmail.com",
    "phone": "210-744-5991",
    "ATS_score": 92,
    "yearsExperience": 6,
    "degree": "B.Sc Mathematics",
    "previousCompany": "SmartTech",
    "skills": [
      "Python"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Aditya Singh",
    "email": "aditya.singh@outlook.com",
    "phone": "232-136-1853",
    "ATS_score": 92,
    "yearsExperience": 7,
    "degree": "MBA",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Angular"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Vivaan Joshi",
    "email": "vivaan.joshi@gmail.com",
    "phone": "117-526-5213",
    "ATS_score": 92,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "DevOps",
      "NoSQL",
      "Go",
      "GraphQL",
      "Angular",
      "Vue",
      "C#"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Avni Singh",
    "email": "avni.singh@yahoo.com",
    "phone": "435-852-3234",
    "ATS_score": 92,
    "yearsExperience": 9,
    "degree": "M.Tech Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "Agile",
      "Machine Learning",
      "HTML",
      "Vue"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Research Scientist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Vihaan Singh",
    "email": "vihaan.singh@outlook.com",
    "phone": "290-966-4936",
    "ATS_score": 92,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Node.js",
      "Scrum",
      "Spring",
      "Ruby"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Vivaan Gupta",
    "email": "vivaan.gupta@yahoo.com",
    "phone": "705-327-2396",
    "ATS_score": 92,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "Agile",
      "Flask"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "System Analyst",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Vivaan Bhat",
    "email": "vivaan.bhat@example.com",
    "phone": "861-192-9651",
    "ATS_score": 93,
    "yearsExperience": 10,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "SQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Arjun Kumar",
    "email": "arjun.kumar@gmail.com",
    "phone": "935-504-6116",
    "ATS_score": 93,
    "yearsExperience": 4,
    "degree": "MBA",
    "previousCompany": "SoftSys",
    "skills": [
      "React",
      "SQL",
      "Kubernetes"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Krishna Gupta",
    "email": "krishna.gupta@example.com",
    "phone": "867-336-5313",
    "ATS_score": 93,
    "yearsExperience": 3,
    "degree": "MCA",
    "previousCompany": "FutureTech",
    "skills": [
      "Agile"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Avni Chopra",
    "email": "avni.chopra@outlook.com",
    "phone": "179-469-3830",
    "ATS_score": 93,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "InnovateX",
    "skills": [
      "React",
      "CSS",
      "Data Science",
      "Spring",
      "C#",
      "Ruby"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Diya Gupta",
    "email": "diya.gupta@gmail.com",
    "phone": "554-419-2462",
    "ATS_score": 93,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechCorp",
    "skills": [
      "React",
      "Angular",
      "TypeScript",
      "C#",
      "Docker"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Aarav Joshi",
    "email": "aarav.joshi@outlook.com",
    "phone": "499-826-3935",
    "ATS_score": 93,
    "yearsExperience": 2,
    "degree": "B.E Electronics",
    "previousCompany": "TechCorp",
    "skills": [
      "Python",
      "Vue"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Krishna Menon",
    "email": "krishna.menon@outlook.com",
    "phone": "692-175-6487",
    "ATS_score": 93,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "HTML",
      "TypeScript"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sai Bhat",
    "email": "sai.bhat@gmail.com",
    "phone": "146-983-8975",
    "ATS_score": 93,
    "yearsExperience": 8,
    "degree": "B.E Electronics",
    "previousCompany": "CodeCrafters",
    "skills": [
      "NoSQL",
      "Scrum",
      "Go"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Reyansh Singh",
    "email": "reyansh.singh@outlook.com",
    "phone": "838-296-3950",
    "ATS_score": 93,
    "yearsExperience": 0,
    "degree": "M.Tech Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Vue"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Software Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Myra Iyer",
    "email": "myra.iyer@outlook.com",
    "phone": "562-894-6793",
    "ATS_score": 93,
    "yearsExperience": 10,
    "degree": "PhD Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Spring"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Sara Menon",
    "email": "sara.menon@gmail.com",
    "phone": "473-980-3152",
    "ATS_score": 94,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "AWS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Avni Joshi",
    "email": "avni.joshi@gmail.com",
    "phone": "404-930-9996",
    "ATS_score": 94,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "Node.js"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ananya Menon",
    "email": "ananya.menon@example.com",
    "phone": "813-978-4116",
    "ATS_score": 94,
    "yearsExperience": 8,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "JavaScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Arjun Chowdhury",
    "email": "arjun.chowdhury@yahoo.com",
    "phone": "893-656-7337",
    "ATS_score": 94,
    "yearsExperience": 4,
    "degree": "B.E Electronics",
    "previousCompany": "Visionary Labs",
    "skills": [
      "CSS"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Vivaan Das",
    "email": "vivaan.das@gmail.com",
    "phone": "191-884-4071",
    "ATS_score": 94,
    "yearsExperience": 3,
    "degree": "M.Tech Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "Kubernetes",
      "TypeScript",
      "Node.js",
      "C#",
      "Java",
      "NoSQL",
      "Django"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Diya Pillai",
    "email": "diya.pillai@gmail.com",
    "phone": "816-750-2276",
    "ATS_score": 94,
    "yearsExperience": 9,
    "degree": "B.Sc Mathematics",
    "previousCompany": "InnovateX",
    "skills": [
      "React",
      "NoSQL",
      "TypeScript",
      "Flask",
      "HTML",
      "Vue"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ira Bhat",
    "email": "ira.bhat@outlook.com",
    "phone": "729-450-9609",
    "ATS_score": 94,
    "yearsExperience": 4,
    "degree": "B.Sc Mathematics",
    "previousCompany": "Data Insights",
    "skills": [
      "Git",
      "Azure"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Ananya Kumar",
    "email": "ananya.kumar@example.com",
    "phone": "670-650-7443",
    "ATS_score": 94,
    "yearsExperience": 7,
    "degree": "B.Sc Information Technology",
    "previousCompany": "TechWave",
    "skills": [
      "Kubernetes",
      "NoSQL"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ishaan Chopra",
    "email": "ishaan.chopra@outlook.com",
    "phone": "796-899-1200",
    "ATS_score": 94,
    "yearsExperience": 9,
    "degree": "MBA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Spring",
      "Kubernetes",
      "Vue",
      "C#",
      "Angular"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Reyansh Roy",
    "email": "reyansh.roy@gmail.com",
    "phone": "269-401-5639",
    "ATS_score": 94,
    "yearsExperience": 6,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Data Insights",
    "skills": [
      "Node.js",
      "React",
      "Spring",
      "Azure",
      "Docker"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Arjun Chowdhury",
    "email": "arjun.chowdhury@example.com",
    "phone": "823-381-8433",
    "ATS_score": 95,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DevSolutions",
    "skills": [
      "Django",
      "Git"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Kavya Joshi",
    "email": "kavya.joshi@gmail.com",
    "phone": "208-668-3111",
    "ATS_score": 95,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Angular"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Saanvi Gupta",
    "email": "saanvi.gupta@example.com",
    "phone": "264-756-9641",
    "ATS_score": 95,
    "yearsExperience": 0,
    "degree": "B.Sc Mathematics",
    "previousCompany": "DataWorks",
    "skills": [
      "Azure",
      "C#",
      "Ruby",
      "TypeScript",
      "Python"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Myra Joshi",
    "email": "myra.joshi@yahoo.com",
    "phone": "336-714-1004",
    "ATS_score": 95,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Creative Minds",
    "skills": [
      "HTML",
      "Ruby",
      "Flask"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Aditya Reddy",
    "email": "aditya.reddy@yahoo.com",
    "phone": "145-763-3072",
    "ATS_score": 95,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "Vue",
      "Java",
      "NoSQL",
      "Node.js",
      "DevOps"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ananya Joshi",
    "email": "ananya.joshi@example.com",
    "phone": "207-549-1240",
    "ATS_score": 95,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "NexGen",
    "skills": [
      "Python",
      "GraphQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Data Scientist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Sai Patel",
    "email": "sai.patel@outlook.com",
    "phone": "614-457-1622",
    "ATS_score": 95,
    "yearsExperience": 1,
    "degree": "B.Sc Mathematics",
    "previousCompany": "FutureTech",
    "skills": [
      "AWS",
      "Node.js",
      "HTML",
      "CSS"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Aarya Kumar",
    "email": "aarya.kumar@example.com",
    "phone": "519-335-3565",
    "ATS_score": 95,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "DataWorks",
    "skills": [
      "SQL",
      "NoSQL",
      "React",
      "Git",
      "Django"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Ananya Joshi",
    "email": "ananya.joshi@outlook.com",
    "phone": "554-831-8181",
    "ATS_score": 95,
    "yearsExperience": 7,
    "degree": "MCA",
    "previousCompany": "DataWorks",
    "skills": [
      "GraphQL"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Ishaan Chopra",
    "email": "ishaan.chopra@yahoo.com",
    "phone": "561-517-2424",
    "ATS_score": 95,
    "yearsExperience": 5,
    "degree": "MCA",
    "previousCompany": "TechWave",
    "skills": [
      "Django",
      "HTML",
      "Machine Learning"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ira Sharma",
    "email": "ira.sharma@yahoo.com",
    "phone": "854-936-5766",
    "ATS_score": 96,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "DevSolutions",
    "skills": [
      "AWS"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Aarya Chowdhury",
    "email": "aarya.chowdhury@example.com",
    "phone": "743-640-7198",
    "ATS_score": 96,
    "yearsExperience": 7,
    "degree": "MCA",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Vue",
      "Scrum"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Diya Chowdhury",
    "email": "diya.chowdhury@yahoo.com",
    "phone": "446-900-3598",
    "ATS_score": 96,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "SQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Trainee"
  },
  {
    "name": "Myra Reddy",
    "email": "myra.reddy@outlook.com",
    "phone": "457-407-8627",
    "ATS_score": 96,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Machine Learning",
      "GraphQL",
      "Ruby",
      "Kubernetes"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Kavya Gupta",
    "email": "kavya.gupta@example.com",
    "phone": "532-345-9813",
    "ATS_score": 96,
    "yearsExperience": 1,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "React",
      "Azure",
      "Flask",
      "AWS",
      "DevOps"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Junior Developer"
  },
  {
    "name": "Sai Patel",
    "email": "sai.patel@outlook.com",
    "phone": "845-408-8795",
    "ATS_score": 96,
    "yearsExperience": 4,
    "degree": "MCA",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Kubernetes",
      "Vue",
      "Python",
      "AWS",
      "Agile",
      "Machine Learning",
      "JavaScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Ishaan Singh",
    "email": "ishaan.singh@example.com",
    "phone": "433-671-4408",
    "ATS_score": 96,
    "yearsExperience": 3,
    "degree": "B.Sc Information Technology",
    "previousCompany": "DataWorks",
    "skills": [
      "Python",
      "React",
      "Java",
      "DevOps",
      "Django",
      "SQL",
      "Angular"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Ananya Mehta",
    "email": "ananya.mehta@outlook.com",
    "phone": "235-606-1751",
    "ATS_score": 96,
    "yearsExperience": 7,
    "degree": "B.Sc Information Technology",
    "previousCompany": "AlphaTech",
    "skills": [
      "Python"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Diya Roy",
    "email": "diya.roy@yahoo.com",
    "phone": "177-876-2946",
    "ATS_score": 96,
    "yearsExperience": 9,
    "degree": "PhD Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "Node.js"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Avni Singh",
    "email": "avni.singh@outlook.com",
    "phone": "689-314-8449",
    "ATS_score": 96,
    "yearsExperience": 3,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "Spring",
      "Rust",
      "CSS",
      "Machine Learning",
      "GraphQL",
      "JavaScript",
      "Python"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "System Analyst",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Saanvi Reddy",
    "email": "saanvi.reddy@yahoo.com",
    "phone": "872-909-5661",
    "ATS_score": 97,
    "yearsExperience": 5,
    "degree": "MBA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Flask",
      "DevOps",
      "Spring"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ira Sharma",
    "email": "ira.sharma@example.com",
    "phone": "621-161-8268",
    "ATS_score": 97,
    "yearsExperience": 5,
    "degree": "PhD Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "Node.js",
      "TypeScript"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Arjun Pillai",
    "email": "arjun.pillai@gmail.com",
    "phone": "503-777-2924",
    "ATS_score": 97,
    "yearsExperience": 6,
    "degree": "M.Tech Computer Science",
    "previousCompany": "TechCorp",
    "skills": [
      "Docker"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Sara Roy",
    "email": "sara.roy@outlook.com",
    "phone": "738-331-5280",
    "ATS_score": 97,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Digital Solutions",
    "skills": [
      "Rust"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Priya Chopra",
    "email": "priya.chopra@gmail.com",
    "phone": "897-875-5024",
    "ATS_score": 97,
    "yearsExperience": 1,
    "degree": "B.E Electronics",
    "previousCompany": "TechWave",
    "skills": [
      "React"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "UI/UX Designer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Aditya Menon",
    "email": "aditya.menon@outlook.com",
    "phone": "588-842-3914",
    "ATS_score": 97,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Azure",
      "DevOps",
      "Kubernetes"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Krishna Verma",
    "email": "krishna.verma@outlook.com",
    "phone": "212-298-5343",
    "ATS_score": 97,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Rust",
      "Go",
      "Angular",
      "Git",
      "Flask",
      "React",
      "DevOps"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Ananya Sharma",
    "email": "ananya.sharma@gmail.com",
    "phone": "460-342-3582",
    "ATS_score": 97,
    "yearsExperience": 8,
    "degree": "B.Sc Information Technology",
    "previousCompany": "NextGen Innovations",
    "skills": [
      "DevOps",
      "Ruby"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ananya Chopra",
    "email": "ananya.chopra@yahoo.com",
    "phone": "667-366-7973",
    "ATS_score": 97,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "NexGen",
    "skills": [
      "JavaScript",
      "C#",
      "Docker",
      "CSS",
      "Java",
      "Angular",
      "TypeScript"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aarya Chopra",
    "email": "aarya.chopra@yahoo.com",
    "phone": "811-519-4135",
    "ATS_score": 97,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "SmartTech",
    "skills": [
      "Docker",
      "Machine Learning",
      "Kubernetes",
      "SQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Aditya Bhat",
    "email": "aditya.bhat@example.com",
    "phone": "926-285-8744",
    "ATS_score": 98,
    "yearsExperience": 2,
    "degree": "B.Sc Mathematics",
    "previousCompany": "TechWave",
    "skills": [
      "Spring",
      "Angular",
      "Agile",
      "DevOps",
      "SQL",
      "Java",
      "NoSQL"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Network Administrator",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Vihaan Roy",
    "email": "vihaan.roy@example.com",
    "phone": "931-426-9665",
    "ATS_score": 98,
    "yearsExperience": 5,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Docker",
      "Angular",
      "Scrum",
      "Django"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Project Coordinator"
  },
  {
    "name": "Avni Singh",
    "email": "avni.singh@outlook.com",
    "phone": "219-655-9439",
    "ATS_score": 98,
    "yearsExperience": 4,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Quantum Dynamics",
    "skills": [
      "AWS",
      "SQL",
      "Scrum"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Vivaan Jain",
    "email": "vivaan.jain@gmail.com",
    "phone": "829-498-3177",
    "ATS_score": 98,
    "yearsExperience": 8,
    "degree": "B.Sc Information Technology",
    "previousCompany": "FutureTech",
    "skills": [
      "GraphQL",
      "Go",
      "Scrum",
      "NoSQL",
      "Django",
      "HTML"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Intern"
  },
  {
    "name": "Aditya Mehta",
    "email": "aditya.mehta@gmail.com",
    "phone": "887-115-9659",
    "ATS_score": 98,
    "yearsExperience": 7,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Creative Minds",
    "skills": [
      "Python",
      "React",
      "Azure",
      "NoSQL",
      "Kubernetes",
      "C#"
    ],
    "summary": "Proven ability to lead projects from conception to deployment.",
    "jobTitle": "Product Manager",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ira Verma",
    "email": "ira.verma@gmail.com",
    "phone": "680-189-4645",
    "ATS_score": 98,
    "yearsExperience": 8,
    "degree": "MBA",
    "previousCompany": "TechWave",
    "skills": [
      "NoSQL",
      "Go",
      "C#",
      "GraphQL",
      "Node.js",
      "Machine Learning"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Cloud Engineer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Krishna Roy",
    "email": "krishna.roy@gmail.com",
    "phone": "962-717-7996",
    "ATS_score": 98,
    "yearsExperience": 1,
    "degree": "MBA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Flask",
      "Vue",
      "HTML",
      "React",
      "Django",
      "Java"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ishaan Singh",
    "email": "ishaan.singh@outlook.com",
    "phone": "643-432-6991",
    "ATS_score": 98,
    "yearsExperience": 2,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Global Solutions",
    "skills": [
      "C#",
      "Go"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Diya Kumar",
    "email": "diya.kumar@gmail.com",
    "phone": "932-641-8962",
    "ATS_score": 98,
    "yearsExperience": 10,
    "degree": "B.E Electronics",
    "previousCompany": "Creative Minds",
    "skills": [
      "JavaScript",
      "Django",
      "Python",
      "Ruby"
    ],
    "summary": "Strong background in software development and troubleshooting.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Business Analyst"
  },
  {
    "name": "Reyansh Das",
    "email": "reyansh.das@yahoo.com",
    "phone": "226-662-3969",
    "ATS_score": 98,
    "yearsExperience": 10,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Synergy Technologies",
    "skills": [
      "Angular",
      "Ruby",
      "Node.js",
      "NoSQL",
      "AWS",
      "Scrum"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Ananya Verma",
    "email": "ananya.verma@example.com",
    "phone": "826-754-3938",
    "ATS_score": 99,
    "yearsExperience": 3,
    "degree": "MBA",
    "previousCompany": "TechCorp",
    "skills": [
      "Docker"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "SEO Specialist",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Ira Reddy",
    "email": "ira.reddy@yahoo.com",
    "phone": "456-775-3514",
    "ATS_score": 99,
    "yearsExperience": 8,
    "degree": "MBA",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "AWS",
      "JavaScript",
      "SQL",
      "GraphQL"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Web Developer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Reyansh Kumar",
    "email": "reyansh.kumar@yahoo.com",
    "phone": "354-535-3045",
    "ATS_score": 99,
    "yearsExperience": 6,
    "degree": "MBA",
    "previousCompany": "SoftSys",
    "skills": [
      "Vue",
      "Node.js",
      "Machine Learning",
      "Flask",
      "Docker"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Krishna Iyer",
    "email": "krishna.iyer@example.com",
    "phone": "174-132-4852",
    "ATS_score": 99,
    "yearsExperience": 6,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Agile"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Game Developer",
    "previousJobRole": "Help Desk Technician"
  },
  {
    "name": "Ayaan Patel",
    "email": "ayaan.patel@example.com",
    "phone": "699-204-4281",
    "ATS_score": 99,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "FutureTech",
    "skills": [
      "AWS",
      "Rust",
      "Spring",
      "Scrum"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ira Gupta",
    "email": "ira.gupta@outlook.com",
    "phone": "940-839-5539",
    "ATS_score": 99,
    "yearsExperience": 6,
    "degree": "B.Sc Information Technology",
    "previousCompany": "Creative Minds",
    "skills": [
      "AWS",
      "Java",
      "React"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "System Administrator"
  },
  {
    "name": "Avni Nair",
    "email": "avni.nair@outlook.com",
    "phone": "944-378-9711",
    "ATS_score": 99,
    "yearsExperience": 7,
    "degree": "PhD Computer Science",
    "previousCompany": "SoftSys",
    "skills": [
      "React",
      "NoSQL",
      "Azure",
      "Django",
      "Machine Learning",
      "Spring"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Sales Associate"
  },
  {
    "name": "Sara Chopra",
    "email": "sara.chopra@outlook.com",
    "phone": "681-388-8580",
    "ATS_score": 99,
    "yearsExperience": 8,
    "degree": "B.Tech Computer Science",
    "previousCompany": "CodeCrafters",
    "skills": [
      "DevOps",
      "C#"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Marketing Intern"
  },
  {
    "name": "Aarya Chowdhury",
    "email": "aarya.chowdhury@gmail.com",
    "phone": "961-393-6303",
    "ATS_score": 99,
    "yearsExperience": 0,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SmartTech",
    "skills": [
      "DevOps",
      "Docker",
      "Agile",
      "Kubernetes",
      "Django"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Research Assistant"
  },
  {
    "name": "Krishna Sharma",
    "email": "krishna.sharma@yahoo.com",
    "phone": "218-632-5276",
    "ATS_score": 99,
    "yearsExperience": 5,
    "degree": "B.E Electronics",
    "previousCompany": "SmartTech",
    "skills": [
      "C#"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Content Strategist",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Kavya Verma",
    "email": "kavya.verma@yahoo.com",
    "phone": "337-807-8148",
    "ATS_score": 100,
    "yearsExperience": 4,
    "degree": "B.Sc Information Technology",
    "previousCompany": "SoftSys",
    "skills": [
      "Rust",
      "Angular",
      "Java",
      "Agile",
      "Git",
      "TypeScript"
    ],
    "summary": "Experienced professional skilled in developing scalable applications.",
    "jobTitle": "Cybersecurity Analyst",
    "previousJobRole": "Data Entry Clerk"
  },
  {
    "name": "Sai Gupta",
    "email": "sai.gupta@outlook.com",
    "phone": "114-392-4187",
    "ATS_score": 100,
    "yearsExperience": 6,
    "degree": "PhD Computer Science",
    "previousCompany": "SmartTech",
    "skills": [
      "Python",
      "Azure",
      "CSS",
      "Angular",
      "HTML",
      "Scrum"
    ],
    "summary": "No professional experience yet, eager to learn.",
    "jobTitle": "DevOps Engineer",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Vivaan Nair",
    "email": "vivaan.nair@gmail.com",
    "phone": "456-426-1105",
    "ATS_score": 100,
    "yearsExperience": 3,
    "degree": "PhD Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "Angular"
    ],
    "summary": "Skilled in both frontend and backend technologies.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Arjun Sharma",
    "email": "arjun.sharma@gmail.com",
    "phone": "522-288-7957",
    "ATS_score": 100,
    "yearsExperience": 2,
    "degree": "MCA",
    "previousCompany": "Global Solutions",
    "skills": [
      "TypeScript",
      "C#",
      "Django",
      "AWS"
    ],
    "summary": "Demonstrated expertise in agile project delivery and team collaboration.",
    "jobTitle": "Quality Assurance Engineer",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Ira Singh",
    "email": "ira.singh@outlook.com",
    "phone": "883-355-4780",
    "ATS_score": 100,
    "yearsExperience": 0,
    "degree": "MBA",
    "previousCompany": "Global Solutions",
    "skills": [
      "NoSQL",
      "Data Science",
      "Kubernetes",
      "Java"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Product Manager",
    "previousJobRole": "Intern"
  },
  {
    "name": "Ishaan Kapoor",
    "email": "ishaan.kapoor@gmail.com",
    "phone": "871-724-1262",
    "ATS_score": 100,
    "yearsExperience": 8,
    "degree": "M.Tech Computer Science",
    "previousCompany": "Cloud Innovations",
    "skills": [
      "Flask",
      "Git",
      "Spring",
      "AWS"
    ],
    "summary": "Adept at working in fast-paced environments with tight deadlines.",
    "jobTitle": "Project Manager",
    "previousJobRole": "Graphic Designer"
  },
  {
    "name": "Arjun Sharma",
    "email": "arjun.sharma@yahoo.com",
    "phone": "508-853-7793",
    "ATS_score": 100,
    "yearsExperience": 1,
    "degree": "PhD Computer Science",
    "previousCompany": "Visionary Labs",
    "skills": [
      "CSS",
      "Rust",
      "Angular",
      "Java",
      "Go"
    ],
    "summary": "Committed to writing clean, efficient, and maintainable code.",
    "jobTitle": "Database Administrator",
    "previousJobRole": "Software Tester"
  },
  {
    "name": "Ishaan Bhat",
    "email": "ishaan.bhat@outlook.com",
    "phone": "771-417-7971",
    "ATS_score": 100,
    "yearsExperience": 6,
    "degree": "B.E Electronics",
    "previousCompany": "Pioneer Systems",
    "skills": [
      "Java"
    ],
    "summary": "Focused on delivering user-centric solutions.",
    "jobTitle": "Technical Writer",
    "previousJobRole": "Technical Support"
  },
  {
    "name": "Reyansh Gupta",
    "email": "reyansh.gupta@outlook.com",
    "phone": "454-292-4799",
    "ATS_score": 100,
    "yearsExperience": 8,
    "degree": "B.Tech Computer Science",
    "previousCompany": "InnovateX",
    "skills": [
      "DevOps",
      "Java",
      "Ruby",
      "Azure",
      "C#"
    ],
    "summary": "Excellent problem-solving and analytical skills.",
    "jobTitle": "Business Analyst",
    "previousJobRole": "Customer Service Representative"
  },
  {
    "name": "Sai Chopra",
    "email": "sai.chopra@yahoo.com",
    "phone": "124-631-2683",
    "ATS_score": 100,
    "yearsExperience": 6,
    "degree": "B.Tech Computer Science",
    "previousCompany": "AlphaTech",
    "skills": [
      "Python",
      "TypeScript",
      "CSS",
      "Java"
    ],
    "summary": "Passionate about technology and continuously learning new skills.",
    "jobTitle": "Mobile App Developer",
    "previousJobRole": "Data Entry Clerk"
  }

]

# Convert to DataFrame
df = pd.DataFrame(initial_resumes)

# Fill missing values properly to avoid errors in filters
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna('')
    else:
        df[col] = df[col].fillna(0)

# Streamlit app configuration for a clean modern look
st.set_page_config(page_title="Advanced ATS Score Tracker", layout="wide")

st.title("🎯 Advanced ATS Score Tracker")
st.markdown("Upload or use your dataset with ATS scores, filter candidates efficiently, and visualize insights.")

# Helper functions to get unique filter options safely
def get_unique_values(column):
    if not df.empty and column in df.columns:
        return sorted(df[column].dropna().unique())
    return []

def get_unique_skills():
    all_skills = []
    if not df.empty and 'skills' in df.columns:
        for skills_list in df['skills']:
            if isinstance(skills_list, list):
                all_skills.extend([skill.strip() for skill in skills_list if skill.strip()])
    return sorted(set(all_skills))

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    selected_names = st.multiselect("Candidates", get_unique_values('name') if not df.empty else ["No candidates available"])
    selected_companies = st.multiselect("Previous Company", get_unique_values('previousCompany') if not df.empty else ["No companies available"])
    selected_degrees = st.multiselect("Degree", get_unique_values('degree') if not df.empty else ["No degrees available"])
    selected_job_titles = st.multiselect("Job Title", get_unique_values('jobTitle') if not df.empty else ["No job titles available"])
    selected_previous_roles = st.multiselect("Previous Job Role", get_unique_values('previousJobRole') if not df.empty else ["No roles available"])
    
    min_exp = int(df['yearsExperience'].min()) if ('yearsExperience' in df.columns and not df.empty) else 0
    max_exp = int(df['yearsExperience'].max()) if ('yearsExperience' in df.columns and not df.empty) else 10
    experience_range = st.slider("Years of Experience", min_exp, max_exp, (min_exp, max_exp))
    
    selected_skills = st.multiselect("Skills", get_unique_skills() if not df.empty else ["No skills available"])
    score_range = st.slider("ATS Score Range", 0, 100, (0, 100))

    apply_filters = st.button("Apply Filters")
    clear_filters = st.button("Clear All")

if clear_filters:
    st.experimental_rerun()

def apply_filters_fn():
    filtered = df.copy()
    if selected_names:
        filtered = filtered[filtered['name'].isin(selected_names)]
    if selected_companies:
        filtered = filtered[filtered['previousCompany'].isin(selected_companies)]
    if selected_degrees:
        filtered = filtered[filtered['degree'].isin(selected_degrees)]
    if selected_job_titles:
        filtered = filtered[filtered['jobTitle'].isin(selected_job_titles)]
    if selected_previous_roles:
        filtered = filtered[filtered['previousJobRole'].isin(selected_previous_roles)]
    if selected_skills:
        def skills_match(skills_list):
            if not isinstance(skills_list, list):
                return False
            return any(skill in skills_list for skill in selected_skills)
        filtered = filtered[filtered['skills'].apply(skills_match)]
    if 'yearsExperience' in filtered.columns:
        filtered = filtered[(filtered['yearsExperience'] >= experience_range[0]) & (filtered['yearsExperience'] <= experience_range[1])]
    if 'ATS_score' in filtered.columns:
        filtered = filtered[(filtered['ATS_score'] >= score_range[0]) & (filtered['ATS_score'] <= score_range[1])]
    return filtered

filtered_df = apply_filters_fn() if apply_filters else df.copy()

if filtered_df.empty:
    st.warning("⚠️ No candidates found with current filters. Please broaden criteria.")
else:
    st.subheader(f"Showing {len(filtered_df)} candidate(s)")

    # Metrics display
    if not filtered_df.empty:
        c1, c2, c3, c4, c5 = st.columns(5)
        
        total_candidates = len(filtered_df)
        average_ats_score = filtered_df['ATS_score'].mean() if 'ATS_score' in filtered_df.columns else 0
        top_ats_score = filtered_df['ATS_score'].max() if 'ATS_score' in filtered_df.columns else 0
        avg_experience = filtered_df['yearsExperience'].mean() if 'yearsExperience' in filtered_df.columns else 0
        unique_companies = filtered_df['previousCompany'].nunique() if 'previousCompany' in filtered_df.columns else 0

        c1.metric("Total Candidates", f"{total_candidates}", delta=str(total_candidates - len(df)))
        c2.metric("Average ATS Score", f"{average_ats_score:.1f}")
        c3.metric("Top ATS Score", f"{top_ats_score}")
        c4.metric("Avg Experience (Years)", f"{avg_experience:.1f}")
        c5.metric("Unique Companies", f"{unique_companies}")
    else:
        st.warning("⚠️ No candidates found to display metrics.")

st.markdown("## 📈 Visualize ATS Scores")

# Update the dropdown to allow multi-selection
attributes = ['ATS_score', 'yearsExperience', 'degree', 'previousCompany', 'skills', 'jobTitle', 'previousJobRole']
selected_attributes = st.multiselect("Choose attributes to visualize", attributes, default=['ATS_score', 'yearsExperience'])

if st.button("Visualize Data"):
    if filtered_df.empty:
        st.info("No data to visualize.")
    else:
        if len(selected_attributes) < 2:
            st.warning("Please select at least two attributes to visualize.")
        else:
            # Example for Bar Chart with two selected attributes
            if 'ATS_score' in selected_attributes and 'degree' in selected_attributes:
                fig = px.bar(filtered_df, x='degree', y='ATS_score', color='degree', hover_data=['skills'],
                             labels={'degree': 'Degree', 'ATS_score': 'ATS Score'},
                             title="ATS Scores by Degree")
                st.plotly_chart(fig, use_container_width=True)
            elif 'yearsExperience' in selected_attributes and 'ATS_score' in selected_attributes:
                fig = px.scatter(filtered_df, x='yearsExperience', y='ATS_score', color='degree', hover_data=['skills'],
                                 labels={'yearsExperience': 'Years of Experience', 'ATS_score': 'ATS Score'},
                                 title="Experience vs ATS Score")
                st.plotly_chart(fig, use_container_width=True)
            # Add more conditions for other combinations of selected attributes
            # For example, you can create pie charts, line charts, etc., based on the selected attributes

st.markdown("---")
st.markdown("""<div style='text-align:center; color:#6b7280; font-size:14px; padding: 1rem;'>
            Advanced ATS Score Tracker — Built with Streamlit</div>""", unsafe_allow_html=True)
