
## The Team
{% for team_member in site.team_members %}
- {{ team_member.name }}
  - role: {{ team_member.role }}
  - grade: {{ team_member.grade }}
{% endfor %}

> "People deserve to know about and be in control of their own software"
