---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '6rem'

sections:
  - block: resume-biography-3
    id: about
    content:
      username: admin
      text: ''
  - block: resume-experience
    content:
      username: admin
    design:
      # Hugo date format
      date_format: 'January 2006'
      # Education or Experience section first?
      is_education_first: false
      columns: '2'
  - block: collection
    id: publications
    content:
      title: Publications
      count: 0
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  - block: collection
    id: conference-talks
    content:
      title: Conference talks
      count: 0
      filters:
        folders:
          - conference-talk
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  - block: collection
    id: posts
    content:
      title: Blog
      subtitle: ''
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 3
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
      filters:
          folders:
           - post
    design:
      # Choose a layout view
      view: compact
      columns: '2'
  - block: collection
    id: games
    content:
      title: Games
      filters:
         folders:
           - project
      # Choose how many pages you would like to display (0 = all pages)
      count: 0
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
       columns: '1'
       view: showcase
---
