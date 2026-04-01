# Design Export Context

- Generated at: `2026-04-01T18:14:16.933Z`
- Document ID: `858267be-699e-405b-9a03-a46e0109dd78`
- Page count: 6

## Original Prompt

```text
Crie uma interface de aplicativo SaaS moderno inspirado no estilo da Netflix, focado em um catálogo de agentes de inteligência artificial.

Nome do app: MuseIA

Objetivo:
Uma central onde usuários exploram agentes de IA organizados dinamicamente a partir de dados vindos de um banco (agentes, perfis e coleções).

IMPORTANTE:
A interface NÃO deve criar categorias fixas.
Ela deve estar preparada para receber dados dinâmicos do backend.

---

🎨 Estilo visual:

- Tema escuro (dark mode)
- Visual estilo Netflix / streaming
- Cards com imagem em destaque
- Hover/efeito de foco (ou destaque ao toque)
- Design limpo, moderno e profissional
- Layout responsivo (mobile e desktop)

---

📱 ESTRUTURA DA HOME

1. Header (topo)
- Logo MuseIA
- Botão "Entrar"
- Botão "Cadastrar"
- Botão "Assinar acesso"

---

2. Barra de busca
- Campo de busca para agentes
- Placeholder: "Buscar agente ou solução..."

---

3. Banner (Hero)
- Título: "Central de Inteligência"
- Subtítulo: "Soluções prontas para resolver problemas reais"
- Botão CTA: "Explorar agentes"
- Botão secundário: "Ativar acesso"

---

4. Seção dinâmica: PERFIS

- Criar um componente de lista horizontal (carrossel ou grid)
- A seção deve ser repetida dinamicamente para cada perfil vindo do backend

Para cada perfil:
- Exibir o nome do perfil como título da seção
- Exibir os agentes vinculados a esse perfil

---

5. Seção dinâmica: COLEÇÕES

- Mesmo comportamento da seção de perfis

Para cada coleção:
- Exibir nome da coleção
- Exibir agentes vinculados

---

6. Card de agente (componente reutilizável)

Cada card deve conter:
- imagem
- nome do agente
- descrição curta
- botão "Acessar"

---

📄 TELA DE DETALHE DO AGENTE

- imagem em destaque
- nome
- descrição completa
- lista de benefícios
- botão principal: "Usar agente"
- mensagem sutil: "Disponível para membros"

---

🔐 COMPORTAMENTO (IMPORTANTE)

A navegação deve ser totalmente livre:

- usuário pode acessar tudo sem login
- pode ver todos os agentes
- pode ver detalhes

---

🚫 BLOQUEIO (somente no botão de uso)

No clique do botão "Usar agente":

- Se não estiver logado:
  → exibir modal ou tela de login/cadastro

- Se estiver logado mas sem acesso ativo:
  → exibir tela ou modal com pagamento (acesso 30 dias)

- Se estiver com acesso:
  → permitir execução (simulado)

---

💳 PAGAMENTO

- NÃO implementar integração real
- Apenas criar interface de incentivo:
  - botão "Ativar acesso"
  - mensagens de conversão ao longo da interface

---

🧩 COMPONENTES NECESSÁRIOS

- Header
- Banner (Hero)
- Barra de busca
- Card de agente (reutilizável)
- Seção dinâmica (lista horizontal)
- Modal de login
- Modal de pagamento

---

🧠 ESTRUTURA PREPARADA PARA BACKEND

- Perfis (lista dinâmica)
- Coleções (lista dinâmica)
- Agentes vinculados a múltiplos perfis e coleções

---

🎯 RESULTADO ESPERADO

Uma interface completa, navegável, moderna e profissional,
com aparência de produto real,
baseada em dados dinâmicos,
com experiência aberta (sem bloqueio inicial)
e monetização apenas no momento de uso do agente.
```

## Theme (JSON)

```json
{
  "fonts": {
    "primary": "google:Plus Jakarta Sans",
    "secondary": "google:Inter"
  },
  "colors": {
    "light": {
      "primary": "#E50914",
      "on_primary": "#FFFFFF",
      "secondary": "#564D4D",
      "on_secondary": "#FFFFFF",
      "accent": "#B81D24",
      "background": "#F5F5F1",
      "surface": "#FFFFFF",
      "on_surface": "#141414",
      "primary_text": "#141414",
      "secondary_text": "#564D4D",
      "hint": "#8C8C8C",
      "error": "#B81D24",
      "on_error": "#FFFFFF",
      "success": "#46D369",
      "divider": "#E5E5E5",
      "transparent": "#00000000"
    },
    "dark": {
      "primary": "#E50914",
      "on_primary": "#FFFFFF",
      "secondary": "#B3B3B3",
      "on_secondary": "#000000",
      "accent": "#E50914",
      "background": "#050505",
      "surface": "#121212",
      "on_surface": "#FFFFFF",
      "primary_text": "#FFFFFF",
      "secondary_text": "#999999",
      "hint": "#666666",
      "error": "#E50914",
      "on_error": "#FFFFFF",
      "success": "#46D369",
      "divider": "#222222",
      "transparent": "#00000000"
    }
  },
  "text_styles": {
    "headline_large": {
      "font": "primary",
      "size": 34,
      "weight": 900,
      "height": 1
    },
    "headline_medium": {
      "font": "primary",
      "size": 28,
      "weight": 800,
      "height": 1.1
    },
    "title_large": {
      "font": "primary",
      "size": 20,
      "weight": 700,
      "height": 1.2
    },
    "title_medium": {
      "font": "primary",
      "size": 16,
      "weight": 700,
      "height": 1.3
    },
    "body_large": {
      "font": "secondary",
      "size": 16,
      "weight": 400,
      "height": 1.5
    },
    "body_medium": {
      "font": "secondary",
      "size": 14,
      "weight": 400,
      "height": 1.5
    },
    "body_small": {
      "font": "secondary",
      "size": 12,
      "weight": 400,
      "height": 1.4
    },
    "label_large": {
      "font": "primary",
      "size": 14,
      "weight": 700,
      "height": 1.2
    },
    "label_medium": {
      "font": "primary",
      "size": 12,
      "weight": 700,
      "height": 1.2
    },
    "label_small": {
      "font": "primary",
      "size": 10,
      "weight": 800,
      "height": 1.1
    }
  },
  "spacing": {
    "xs": 4,
    "sm": 8,
    "md": 16,
    "lg": 24,
    "xl": 32
  },
  "radii": {
    "sm": 4,
    "md": 8,
    "lg": 16,
    "full": 9999
  },
  "shadows": {
    "sm": {
      "color": "#0000004D",
      "dx": 0,
      "dy": 2,
      "blur": 4,
      "spread": 0
    },
    "md": {
      "color": "#00000080",
      "dx": 0,
      "dy": 4,
      "blur": 8,
      "spread": 0
    },
    "lg": {
      "color": "#000000B3",
      "dx": 0,
      "dy": 8,
      "blur": 16,
      "spread": 0
    },
    "xl": {
      "color": "#000000FF",
      "dx": 0,
      "dy": 12,
      "blur": 24,
      "spread": 0
    }
  }
}
```

## Pages

### 1. Home Showcase

- Frame ID: `dd7e9bdd-a3e1-4836-821a-062d54773def`
- Original page prompt: "Netflix-style home with a hero banner, search bar, and dynamic horizontal carousels for Profiles and Collections."
- Follow-up prompts: _None_

#### DslDocument (JSON)

```json
{
  "root": {
    "type": "scaffold",
    "properties": {
      "bg": {
        "color": {
          "color": "background"
        }
      }
    },
    "children": [
      {
        "type": "stack",
        "children": [
          {
            "type": "column",
            "properties": {
              "scroll": {
                "boolVal": {
                  "value": true
                }
              },
              "cross_align": {
                "align": {
                  "named": "stretch"
                }
              },
              "spacing": {
                "stringVal": {
                  "value": "xl"
                }
              }
            },
            "children": [
              {
                "type": "stack",
                "properties": {
                  "height": {
                    "px": {
                      "value": 480,
                      "isInfinity": false
                    }
                  }
                },
                "children": [
                  {
                    "type": "image",
                    "properties": {
                      "source_desc": {
                        "imageSource": {
                          "type": "IMAGE_SOURCE_TYPE_URL",
                          "value": "https://dimg.dreamflow.cloud/v1/image/futuristic+cyberpunk+robot+female+face+neon"
                        }
                      },
                      "fit": {
                        "stringVal": {
                          "value": "cover"
                        }
                      },
                      "width": {
                        "px": {
                          "value": "Infinity",
                          "isInfinity": true
                        }
                      },
                      "height": {
                        "px": {
                          "value": 480,
                          "isInfinity": false
                        }
                      }
                    },
                    "editorId": "f41cfe8c-b762-4728-88e4-1fea9f35df29"
                  },
                  {
                    "type": "container",
                    "properties": {
                      "gradient": {
                        "gradient": {
                          "type": "GRADIENT_TYPE_LINEAR",
                          "direction": "to_top",
                          "stops": [
                            {
                              "color": "background",
                              "position": 0
                            },
                            {
                              "color": "background/40",
                              "position": 70
                            },
                            {
                              "color": "transparent",
                              "position": 100
                            }
                          ]
                        }
                      },
                      "width": {
                        "px": {
                          "value": "Infinity",
                          "isInfinity": true
                        }
                      },
                      "height": {
                        "px": {
                          "value": 480,
                          "isInfinity": false
                        }
                      }
                    },
                    "editorId": "0fc3da7f-ea81-4abe-be58-570f482e6da7"
                  },
                  {
                    "type": "column",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "bottom_left"
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "topToken": "xl",
                          "rightToken": "lg",
                          "bottomToken": "xl",
                          "leftToken": "lg"
                        }
                      },
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      },
                      "cross_align": {
                        "align": {
                          "named": "start"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "container",
                        "properties": {
                          "border": {
                            "border": {
                              "width": 1,
                              "color": "primary"
                            }
                          },
                          "padding": {
                            "edgeInsets": {
                              "top": 4,
                              "right": 10,
                              "bottom": 4,
                              "left": 10
                            }
                          },
                          "radius": {
                            "radius": {
                              "topLeft": 0,
                              "topRight": 0,
                              "bottomLeft": 0,
                              "bottomRight": 0,
                              "token": "sm"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "DESTAQUE DA SEMANA"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              }
                            },
                            "editorId": "531a77c7-bc8d-4e21-b2ca-64dd08e40159"
                          }
                        ],
                        "editorId": "d09a4f68-3aa2-4211-bb40-f8c81852a3bf"
                      },
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "MUSEIA\nELITE"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "headline_large"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          }
                        },
                        "editorId": "a8fc5893-f7fe-4f06-b655-ecdfe590f770"
                      },
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Os agentes mais poderosos do planeta,\nagora à sua disposição."
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "body_medium"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "secondary_text"
                            }
                          }
                        },
                        "editorId": "d67a5f5e-a57e-4f36-93f2-269d8d36beaf"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "@std.button",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Explorar Agora"
                                }
                              },
                              "variant": {
                                "stringVal": {
                                  "value": "primary"
                                }
                              },
                              "size": {
                                "stringVal": {
                                  "value": "large"
                                }
                              },
                              "icon": {
                                "stringVal": {
                                  "value": "play_arrow_rounded"
                                }
                              }
                            },
                            "editorId": "f8be5008-0a12-4258-a2b2-c6ccd39b87a3"
                          },
                          {
                            "type": "iconbutton",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "add_rounded"
                                }
                              },
                              "bg": {
                                "color": {
                                  "color": "surface",
                                  "opacityPercent": 30
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "white"
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "full"
                                }
                              },
                              "size": {
                                "numberVal": {
                                  "value": 24
                                }
                              }
                            },
                            "editorId": "91ee1c0f-b946-4c6d-8d60-05bee489f5ce"
                          }
                        ],
                        "editorId": "eeff86db-d5e0-4a21-8163-00ec012e381c"
                      }
                    ],
                    "editorId": "686e1f92-eb28-4db2-94cd-2ad10044cbf0"
                  }
                ],
                "editorId": "1dabbbcf-265d-4007-80df-f2cb52b3cda5"
              },
              {
                "type": "column",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "md"
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "rightToken": "lg",
                      "leftToken": "lg"
                    }
                  }
                },
                "children": [
                  {
                    "type": "@std.textfield",
                    "properties": {
                      "hint": {
                        "stringVal": {
                          "value": "O que você deseja resolver?"
                        }
                      },
                      "leading_icon": {
                        "stringVal": {
                          "value": "search_rounded"
                        }
                      },
                      "variant": {
                        "stringVal": {
                          "value": "filled"
                        }
                      },
                      "bg": {
                        "stringVal": {
                          "value": "surface"
                        }
                      }
                    },
                    "editorId": "4dcc4c28-9a1d-4706-b2fa-3f3054367abc"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "scroll": {
                        "boolVal": {
                          "value": true
                        }
                      },
                      "spacing": {
                        "numberVal": {
                          "value": 0
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "@category_pill",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Produtividade"
                            }
                          }
                        },
                        "editorId": "5cbd1c50-5a30-4186-8aa1-de6c21b9b067"
                      },
                      {
                        "type": "@category_pill",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Marketing"
                            }
                          }
                        },
                        "editorId": "91fcc418-3928-4292-b8d9-01492cc7cd8d"
                      },
                      {
                        "type": "@category_pill",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Código"
                            }
                          }
                        },
                        "editorId": "8eab8db0-22b0-44fe-80bb-5581dca926c4"
                      },
                      {
                        "type": "@category_pill",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Design"
                            }
                          }
                        },
                        "editorId": "6f2c6b98-2641-4a23-aea8-a09d721d7d84"
                      }
                    ],
                    "editorId": "68e4f909-bcb6-4d05-98a4-018a0cb3b09b"
                  }
                ],
                "editorId": "8df32a42-d7b5-47a3-889a-7b888e93d1d2"
              },
              {
                "type": "column",
                "properties": {
                  "cross_align": {
                    "align": {
                      "named": "stretch"
                    }
                  }
                },
                "children": [
                  {
                    "type": "@section_header",
                    "properties": {
                      "title": {
                        "stringVal": {
                          "value": "Perfis Criativos"
                        }
                      }
                    },
                    "editorId": "951650d3-28fc-4a72-a465-b740ab20c706"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "scroll": {
                        "boolVal": {
                          "value": true
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "rightToken": "lg",
                          "leftToken": "lg"
                        }
                      },
                      "spacing": {
                        "numberVal": {
                          "value": 0
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Art Gen"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Transforme texto em obras primas"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "digital art robot"
                            }
                          }
                        },
                        "editorId": "e4eeebfc-d7d8-4d75-b4e3-e101cea6cf56"
                      },
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Copy Master"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Textos que convertem em segundos"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "typewriter robot"
                            }
                          }
                        },
                        "editorId": "ca5b9445-ed79-458f-8806-d40b253f7bf1"
                      },
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Video Edit"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Cortes dinâmicos automáticos"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "cinema robot"
                            }
                          }
                        },
                        "editorId": "ecf7b7bf-554d-4aed-a9df-a05ded97777a"
                      },
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Sound Lab"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Trilhas sonoras exclusivas"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "music studio robot"
                            }
                          }
                        },
                        "editorId": "eaa7a892-94f7-439a-aba7-fd809ea91435"
                      }
                    ],
                    "editorId": "bd88573e-56d0-4ae8-836e-4153c99ecdcf"
                  }
                ],
                "editorId": "d8c76158-1b54-47cf-8e50-9002db6173c2"
              },
              {
                "type": "container",
                "properties": {
                  "margin": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "rightToken": "lg",
                      "leftToken": "lg"
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "xl"
                    }
                  },
                  "radius": {
                    "radius": {
                      "topLeft": 0,
                      "topRight": 0,
                      "bottomLeft": 0,
                      "bottomRight": 0,
                      "token": "lg"
                    }
                  },
                  "gradient": {
                    "gradient": {
                      "type": "GRADIENT_TYPE_LINEAR",
                      "direction": "135",
                      "stops": [
                        {
                          "color": "primary"
                        },
                        {
                          "color": "accent"
                        }
                      ]
                    }
                  },
                  "shadow": {
                    "stringVal": {
                      "value": "lg"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "column",
                        "properties": {
                          "expanded": {
                            "expanded": {
                              "enabled": true,
                              "flex": 1
                            }
                          },
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          },
                          "spacing": {
                            "stringVal": {
                              "value": "sm"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "DESBLOQUEIE O FUTURO"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "title_medium"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              }
                            },
                            "editorId": "f20f52dd-cc9f-4784-8457-132e7c796829"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Acesso ilimitado a todos os agentes por 30 dias."
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "body_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary",
                                  "opacityPercent": 80
                                }
                              }
                            },
                            "editorId": "5764b3c7-6c3d-44a1-9568-3969d3e19fff"
                          },
                          {
                            "type": "@std.button",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Ativar Acesso"
                                }
                              },
                              "variant": {
                                "stringVal": {
                                  "value": "secondary"
                                }
                              },
                              "size": {
                                "stringVal": {
                                  "value": "small"
                                }
                              }
                            },
                            "editorId": "c8b788c0-5c08-42b0-a7be-ba8f8ba5ef06"
                          }
                        ],
                        "editorId": "f738788e-d32d-47d8-a1ff-a348307c0a28"
                      },
                      {
                        "type": "icon",
                        "properties": {
                          "name": {
                            "icon": {
                              "name": "auto_awesome_rounded"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "on_primary"
                            }
                          },
                          "size": {
                            "numberVal": {
                              "value": 48
                            }
                          },
                          "opacity": {
                            "numberVal": {
                              "value": 0.5
                            }
                          }
                        },
                        "editorId": "e5325f0b-f053-4dc1-b542-007e0affc574"
                      }
                    ],
                    "editorId": "27746aae-90bf-49b9-82c8-cefb7acedf84"
                  }
                ],
                "editorId": "194cad3b-e526-4746-a485-4a91393ddd5b"
              },
              {
                "type": "column",
                "properties": {
                  "cross_align": {
                    "align": {
                      "named": "stretch"
                    }
                  }
                },
                "children": [
                  {
                    "type": "@section_header",
                    "properties": {
                      "title": {
                        "stringVal": {
                          "value": "Coleções Tech"
                        }
                      }
                    },
                    "editorId": "931331ba-49ae-4bcb-be8b-157d62f51353"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "scroll": {
                        "boolVal": {
                          "value": true
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "rightToken": "lg",
                          "leftToken": "lg"
                        }
                      },
                      "spacing": {
                        "numberVal": {
                          "value": 0
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Bug Hunter"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Depuração de código complexo"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "circuit robot"
                            }
                          }
                        },
                        "editorId": "d647d540-6146-46d1-b8ba-6375a7b1de34"
                      },
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Data Viz"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Dashboards de outro mundo"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "hologram graph robot"
                            }
                          }
                        },
                        "editorId": "2421ad45-50f7-4dde-9d07-86b6febbdacd"
                      },
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Cloud Architect"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Infraestrutura escalável"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "cloud server robot"
                            }
                          }
                        },
                        "editorId": "f7f66269-ed0d-4a1f-ace8-2b841960bfca"
                      },
                      {
                        "type": "@immersive_agent_card",
                        "properties": {
                          "name": {
                            "stringVal": {
                              "value": "Security Bot"
                            }
                          },
                          "desc": {
                            "stringVal": {
                              "value": "Auditoria de vulnerabilidades"
                            }
                          },
                          "img_desc": {
                            "stringVal": {
                              "value": "shield robot"
                            }
                          }
                        },
                        "editorId": "7870d8eb-5b4a-48ce-a54a-40fd2dabb0a4"
                      }
                    ],
                    "editorId": "47985448-6264-4b9b-8f0a-a846a51702b5"
                  }
                ],
                "editorId": "3b95f709-5a86-4aed-8184-9a8b3850a614"
              },
              {
                "type": "sizedbox",
                "properties": {
                  "height": {
                    "stringVal": {
                      "value": "xl"
                    }
                  }
                },
                "editorId": "84ba53e6-bbfe-43a9-bec0-c4939fcf6048"
              }
            ],
            "editorId": "0083da9b-6190-42b4-8f12-3d37b3974fdc"
          },
          {
            "type": "container",
            "properties": {
              "height": {
                "px": {
                  "value": 100,
                  "isInfinity": false
                }
              },
              "width": {
                "px": {
                  "value": "Infinity",
                  "isInfinity": true
                }
              },
              "align_y": {
                "numberVal": {
                  "value": -1
                }
              },
              "gradient": {
                "gradient": {
                  "type": "GRADIENT_TYPE_LINEAR",
                  "direction": "to_bottom",
                  "stops": [
                    {
                      "color": "background"
                    },
                    {
                      "color": "background/0"
                    }
                  ]
                }
              },
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "rightToken": "lg",
                  "leftToken": "lg"
                }
              }
            },
            "children": [
              {
                "type": "row",
                "properties": {
                  "align": {
                    "align": {
                      "named": "space_between"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "center"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "xs"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "logo_icon",
                        "properties": {
                          "name": {
                            "icon": {
                              "name": "openai"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary"
                            }
                          },
                          "size": {
                            "numberVal": {
                              "value": 24
                            }
                          }
                        },
                        "editorId": "693d1804-e505-43c6-ba61-64a20aaa96bb"
                      },
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "MuseIA"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "title_large"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "font_weight": {
                            "numberVal": {
                              "value": 900
                            }
                          }
                        },
                        "editorId": "e1e05f6a-20c3-43ee-bf11-c419c19cad0a"
                      }
                    ],
                    "editorId": "e92f3669-6bc0-485b-9935-19161fa3cf7e"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "sm"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "@std.button",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Entrar"
                            }
                          },
                          "variant": {
                            "stringVal": {
                              "value": "ghost"
                            }
                          },
                          "size": {
                            "stringVal": {
                              "value": "small"
                            }
                          }
                        },
                        "editorId": "061d459b-f9ad-4955-85d3-cdbfe4a03c6b"
                      },
                      {
                        "type": "@std.button",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Assinar"
                            }
                          },
                          "variant": {
                            "stringVal": {
                              "value": "primary"
                            }
                          },
                          "size": {
                            "stringVal": {
                              "value": "small"
                            }
                          }
                        },
                        "editorId": "06cc4a57-b649-45a4-93f1-9c98c3464c01"
                      }
                    ],
                    "editorId": "59787027-24af-4258-a6df-bd39298efb15"
                  }
                ],
                "editorId": "5b3e27c6-cd83-4644-837b-6a7d4af9e2bd"
              }
            ],
            "editorId": "461d9df7-c0e6-498e-9ca3-e2dcb73429bb"
          }
        ],
        "editorId": "28af4408-f022-4206-b05e-9c02dca6d6ea"
      }
    ],
    "editorId": "3b3f6211-d102-4847-9a30-4a0b9e1a4eb8"
  }
}
```

### 2. Agent Details

- Frame ID: `f6e9414e-c8ea-4fe7-af9e-6481a02d5db6`
- Original page prompt: "Detailed view of an AI agent featuring a large cover image, full description, list of benefits, and an 'Use Agent' call to action."
- Follow-up prompts: _None_

#### DslDocument (JSON)

```json
{
  "root": {
    "type": "scaffold",
    "properties": {
      "bg": {
        "color": {
          "color": "background"
        }
      }
    },
    "children": [
      {
        "type": "stack",
        "children": [
          {
            "type": "column",
            "properties": {
              "scroll": {
                "boolVal": {
                  "value": true
                }
              },
              "cross_align": {
                "align": {
                  "named": "stretch"
                }
              },
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 120,
                  "left": 0
                }
              }
            },
            "children": [
              {
                "type": "stack",
                "properties": {
                  "height": {
                    "px": {
                      "value": 450,
                      "isInfinity": false
                    }
                  }
                },
                "children": [
                  {
                    "type": "image",
                    "properties": {
                      "source_desc": {
                        "imageSource": {
                          "type": "IMAGE_SOURCE_TYPE_URL",
                          "value": "https://dimg.dreamflow.cloud/v1/image/highly+detailed+futuristic+female+android+face+with+glowing+blue+circuit+lines+cinematic+lighting"
                        }
                      },
                      "fit": {
                        "stringVal": {
                          "value": "cover"
                        }
                      },
                      "width": {
                        "px": {
                          "value": "Infinity",
                          "isInfinity": true
                        }
                      },
                      "height": {
                        "px": {
                          "value": 450,
                          "isInfinity": false
                        }
                      }
                    },
                    "editorId": "d071acac-2475-43bc-87fb-3366006021a7"
                  },
                  {
                    "type": "container",
                    "properties": {
                      "gradient": {
                        "gradient": {
                          "type": "GRADIENT_TYPE_LINEAR",
                          "direction": "to_top",
                          "stops": [
                            {
                              "color": "background",
                              "position": 0
                            },
                            {
                              "color": "background/60",
                              "position": 50
                            },
                            {
                              "color": "transparent",
                              "position": 100
                            }
                          ]
                        }
                      },
                      "width": {
                        "px": {
                          "value": "Infinity",
                          "isInfinity": true
                        }
                      },
                      "height": {
                        "px": {
                          "value": 450,
                          "isInfinity": false
                        }
                      }
                    },
                    "editorId": "088bd99e-1a54-4868-9806-073d1d0fe32e"
                  },
                  {
                    "type": "column",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "bottom_left"
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "topToken": "xl",
                          "rightToken": "lg",
                          "bottomToken": "xl",
                          "leftToken": "lg"
                        }
                      },
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      },
                      "cross_align": {
                        "align": {
                          "named": "start"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "sm"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "container",
                            "properties": {
                              "bg": {
                                "color": {
                                  "color": "primary"
                                }
                              },
                              "padding": {
                                "edgeInsets": {
                                  "top": 4,
                                  "right": 12,
                                  "bottom": 4,
                                  "left": 12
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "full"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "PREMIUM"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "label_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "on_primary"
                                    }
                                  },
                                  "font_weight": {
                                    "stringVal": {
                                      "value": "bold"
                                    }
                                  }
                                },
                                "editorId": "85e76d8c-b630-4f22-81ee-b557fb80b9de"
                              }
                            ],
                            "editorId": "80f35681-06bb-4dec-91db-f38e1c10c66f"
                          },
                          {
                            "type": "@detail_pill",
                            "properties": {
                              "icon": {
                                "stringVal": {
                                  "value": "bolt_rounded"
                                }
                              },
                              "label": {
                                "stringVal": {
                                  "value": "Alta Velocidade"
                                }
                              }
                            },
                            "editorId": "55d8807d-5aef-4882-864c-851d8c4ebb5d"
                          },
                          {
                            "type": "@detail_pill",
                            "properties": {
                              "icon": {
                                "stringVal": {
                                  "value": "verified_user_rounded"
                                }
                              },
                              "label": {
                                "stringVal": {
                                  "value": "Seguro"
                                }
                              }
                            },
                            "editorId": "825bfc92-c320-4968-83a0-cc585a08812c"
                          }
                        ],
                        "editorId": "fa94386f-b70c-46f4-b3ff-aaddfb2d757d"
                      },
                      {
                        "type": "column",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "xs"
                            }
                          },
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "MUSEIA ELITE"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "headline_large"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "primary_text"
                                }
                              },
                              "font_weight": {
                                "numberVal": {
                                  "value": 900
                                }
                              }
                            },
                            "editorId": "9c1e2371-8706-4018-b8d6-52d1740de94d"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Especialista em Estratégia Digital & IA"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "title_medium"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              }
                            },
                            "editorId": "dc8a6792-8f1b-4cb3-af49-037a1eaa295b"
                          }
                        ],
                        "editorId": "ff09a63f-d0d5-4579-81e7-614188ade5c4"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          },
                          "margin": {
                            "edgeInsets": {
                              "top": 0,
                              "right": 0,
                              "bottom": 0,
                              "left": 0,
                              "topToken": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "@std.button",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Usar Agente"
                                }
                              },
                              "variant": {
                                "stringVal": {
                                  "value": "primary"
                                }
                              },
                              "size": {
                                "stringVal": {
                                  "value": "large"
                                }
                              },
                              "icon": {
                                "stringVal": {
                                  "value": "play_arrow_rounded"
                                }
                              },
                              "full_width": {
                                "boolVal": {
                                  "value": true
                                }
                              }
                            },
                            "editorId": "b4c6c505-5859-4b73-9458-7d67d96d3fce"
                          }
                        ],
                        "editorId": "7750a285-236f-4b5c-a685-a23df3b8c03b"
                      }
                    ],
                    "editorId": "19085bfb-166e-4adb-b3a4-280e82018149"
                  },
                  {
                    "type": "container",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "top_left"
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "token": "lg"
                        }
                      },
                      "safe_area_top": {
                        "boolVal": {
                          "value": true
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "iconbutton",
                        "properties": {
                          "name": {
                            "icon": {
                              "name": "arrow_back_ios_new_rounded"
                            }
                          },
                          "bg": {
                            "color": {
                              "color": "surface",
                              "opacityPercent": 40
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "radius": {
                            "radius": {
                              "topLeft": 0,
                              "topRight": 0,
                              "bottomLeft": 0,
                              "bottomRight": 0,
                              "token": "full"
                            }
                          },
                          "size": {
                            "numberVal": {
                              "value": 20
                            }
                          },
                          "backdrop_blur": {
                            "numberVal": {
                              "value": 10
                            }
                          }
                        },
                        "editorId": "cdabdbbb-3337-422a-b0d7-a752d7036329"
                      }
                    ],
                    "editorId": "9b9e5078-186f-4a71-bec4-9f2b9b0e75b4"
                  }
                ],
                "editorId": "dc9f50d5-8872-4204-83f4-e25e645131b9"
              },
              {
                "type": "column",
                "properties": {
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "lg"
                    }
                  },
                  "spacing": {
                    "stringVal": {
                      "value": "xl"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "stretch"
                    }
                  }
                },
                "children": [
                  {
                    "type": "column",
                    "properties": {
                      "cross_align": {
                        "align": {
                          "named": "start"
                        }
                      },
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Sobre o Agente"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "title_large"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "font_weight": {
                            "numberVal": {
                              "value": 700
                            }
                          }
                        },
                        "editorId": "bfce1d99-fc2c-4884-8fb3-97459172c21a"
                      },
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "O MuseIA Elite é o ápice da nossa engenharia de prompts. Treinado em mais de 50.000 cases de sucesso de marketing e tecnologia, este agente não apenas responde perguntas, mas cria estratégias completas de ponta a ponta para o seu negócio."
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "body_large"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "secondary_text"
                            }
                          },
                          "line_height": {
                            "numberVal": {
                              "value": 1.6
                            }
                          }
                        },
                        "editorId": "76acacaf-abcd-4226-97a1-8238e275e845"
                      }
                    ],
                    "editorId": "01dae7cf-ca3d-4e32-8f44-70116dee01ea"
                  },
                  {
                    "type": "column",
                    "properties": {
                      "cross_align": {
                        "align": {
                          "named": "start"
                        }
                      },
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "O que você ganha"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "title_medium"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "font_weight": {
                            "numberVal": {
                              "value": 700
                            }
                          }
                        },
                        "editorId": "7dabef1b-67fd-48ca-8cb4-3f66942c1341"
                      },
                      {
                        "type": "column",
                        "properties": {
                          "cross_align": {
                            "align": {
                              "named": "stretch"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "@benefit_item",
                            "properties": {
                              "text": {
                                "stringVal": {
                                  "value": "Análise de mercado em tempo real com dados globais"
                                }
                              }
                            },
                            "editorId": "4ccd7060-fc59-4474-9b5e-81772736b10a"
                          },
                          {
                            "type": "@benefit_item",
                            "properties": {
                              "text": {
                                "stringVal": {
                                  "value": "Geração de copy de alta conversão para anúncios e landing pages"
                                }
                              }
                            },
                            "editorId": "7cb5b4f9-61a4-4c7e-b527-0e786a900ca2"
                          },
                          {
                            "type": "@benefit_item",
                            "properties": {
                              "text": {
                                "stringVal": {
                                  "value": "Automação de fluxos de trabalho complexos via API"
                                }
                              }
                            },
                            "editorId": "a2bcee18-9a13-4070-a460-13bfd3f92044"
                          },
                          {
                            "type": "@benefit_item",
                            "properties": {
                              "text": {
                                "stringVal": {
                                  "value": "Suporte prioritário 24/7 com processamento neural dedicado"
                                }
                              }
                            },
                            "editorId": "189348db-caea-406e-a33d-4dc32c443a32"
                          }
                        ],
                        "editorId": "46820415-2751-4cb9-aa89-d7bcf12d1337"
                      }
                    ],
                    "editorId": "0cef3dfb-74ea-4d06-b6d6-969d6ceea996"
                  },
                  {
                    "type": "container",
                    "properties": {
                      "bg": {
                        "color": {
                          "color": "surface"
                        }
                      },
                      "radius": {
                        "radius": {
                          "topLeft": 0,
                          "topRight": 0,
                          "bottomLeft": 0,
                          "bottomRight": 0,
                          "token": "lg"
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "token": "lg"
                        }
                      },
                      "border": {
                        "border": {
                          "width": 1,
                          "color": "divider"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "icon",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "info_outline_rounded"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_surface"
                                }
                              },
                              "size": {
                                "numberVal": {
                                  "value": 24
                                }
                              }
                            },
                            "editorId": "085b8339-a342-410c-a167-6691655d5d5a"
                          },
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "column",
                                "properties": {
                                  "cross_align": {
                                    "align": {
                                      "named": "start"
                                    }
                                  },
                                  "spacing": {
                                    "stringVal": {
                                      "value": "xs"
                                    }
                                  }
                                },
                                "children": [
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "Disponível para membros"
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "label_large"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "primary_text"
                                        }
                                      },
                                      "font_weight": {
                                        "numberVal": {
                                          "value": 600
                                        }
                                      }
                                    },
                                    "editorId": "19fd0260-b633-407d-b44e-165dcfc31d21"
                                  },
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "Este agente requer uma assinatura ativa ou passe de 30 dias para execução."
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "body_small"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "secondary_text"
                                        }
                                      }
                                    },
                                    "editorId": "0f627590-5b74-4b2c-be84-11c2ca2cfa1f"
                                  }
                                ],
                                "editorId": "a75ce3b5-d508-4b95-80e0-83f3d340638f"
                              }
                            ],
                            "editorId": "8c25d079-ca96-4765-96c5-72c92dfaaf02"
                          }
                        ],
                        "editorId": "ecd33d0e-1744-4fe6-ab75-6a88c26eee6f"
                      }
                    ],
                    "editorId": "ee97cd03-61f8-4692-b5cc-881e76afc52a"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "space_between"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "column",
                        "properties": {
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          },
                          "spacing": {
                            "stringVal": {
                              "value": "xs"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "MODELO"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              }
                            },
                            "editorId": "50f4c341-1cdf-4a33-9ca1-60ac2a5979df"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Muse-4 Turbo"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "body_medium"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "primary_text"
                                }
                              }
                            },
                            "editorId": "2b1a1674-238e-4491-b4c7-c88dec5c14d4"
                          }
                        ],
                        "editorId": "a1ce7192-41d4-47b3-8428-169ee1b9d042"
                      },
                      {
                        "type": "divider",
                        "properties": {
                          "vertical": {
                            "boolVal": {
                              "value": true
                            }
                          },
                          "height": {
                            "px": {
                              "value": 30,
                              "isInfinity": false
                            }
                          },
                          "color": {
                            "color": {
                              "color": "divider"
                            }
                          }
                        },
                        "editorId": "e549efde-c8e8-4aac-a232-e2e17af528bd"
                      },
                      {
                        "type": "column",
                        "properties": {
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          },
                          "spacing": {
                            "stringVal": {
                              "value": "xs"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "LATÊNCIA"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              }
                            },
                            "editorId": "500d15c0-61e2-41d7-9a10-0a1a3b2be8d0"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "< 1.2s"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "body_medium"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "primary_text"
                                }
                              }
                            },
                            "editorId": "e9bf1c9a-4689-400e-b185-bfbfccf64fa6"
                          }
                        ],
                        "editorId": "a8785ff0-3fbf-46e3-b96a-204c5a31c1a0"
                      },
                      {
                        "type": "divider",
                        "properties": {
                          "vertical": {
                            "boolVal": {
                              "value": true
                            }
                          },
                          "height": {
                            "px": {
                              "value": 30,
                              "isInfinity": false
                            }
                          },
                          "color": {
                            "color": {
                              "color": "divider"
                            }
                          }
                        },
                        "editorId": "27d84a3f-ab37-4470-9284-dcd8c02169e7"
                      },
                      {
                        "type": "column",
                        "properties": {
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          },
                          "spacing": {
                            "stringVal": {
                              "value": "xs"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "VERSÃO"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              }
                            },
                            "editorId": "5c3188e2-cee4-4288-9052-0743b1c461a5"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "v2.4.0"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "body_medium"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "primary_text"
                                }
                              }
                            },
                            "editorId": "0746f7f4-a5c3-4827-b674-d2d27d4fd86d"
                          }
                        ],
                        "editorId": "5d7ac495-e994-43be-8113-2902d8725912"
                      }
                    ],
                    "editorId": "94b2534c-7025-44f0-8290-a11c35bd9d82"
                  }
                ],
                "editorId": "7ea84271-8875-4c43-bc89-fa58bd8a03d6"
              }
            ],
            "editorId": "752e77e2-2091-4f28-8523-8f2bd19581ca"
          },
          {
            "type": "container",
            "properties": {
              "align": {
                "align": {
                  "named": "bottom_center"
                }
              },
              "width": {
                "px": {
                  "value": "Infinity",
                  "isInfinity": true
                }
              },
              "height": {
                "px": {
                  "value": 100,
                  "isInfinity": false
                }
              },
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "topToken": "md",
                  "rightToken": "lg",
                  "bottomToken": "md",
                  "leftToken": "lg"
                }
              },
              "gradient": {
                "gradient": {
                  "type": "GRADIENT_TYPE_LINEAR",
                  "direction": "to_top",
                  "stops": [
                    {
                      "color": "background"
                    },
                    {
                      "color": "background/80"
                    }
                  ]
                }
              }
            },
            "children": [
              {
                "type": "container",
                "properties": {
                  "bg": {
                    "color": {
                      "color": "surface"
                    }
                  },
                  "radius": {
                    "radius": {
                      "topLeft": 0,
                      "topRight": 0,
                      "bottomLeft": 0,
                      "bottomRight": 0,
                      "token": "xl"
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "topToken": "md",
                      "rightToken": "lg",
                      "bottomToken": "md",
                      "leftToken": "lg"
                    }
                  },
                  "shadow": {
                    "stringVal": {
                      "value": "lg"
                    }
                  },
                  "border": {
                    "border": {
                      "width": 1,
                      "color": "divider"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "space_between"
                        }
                      },
                      "cross_align": {
                        "align": {
                          "named": "center"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "column",
                        "properties": {
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          },
                          "main_size": {
                            "stringVal": {
                              "value": "min"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Acesso 30 dias"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "secondary_text"
                                }
                              }
                            },
                            "editorId": "4c9c7e70-fc9f-4d76-874a-8972f128a580"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "R$ 49,90"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "title_medium"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "primary_text"
                                }
                              },
                              "font_weight": {
                                "stringVal": {
                                  "value": "bold"
                                }
                              }
                            },
                            "editorId": "1878444a-cd42-4649-928f-d94bc631c587"
                          }
                        ],
                        "editorId": "709882d6-1fcc-4848-8873-d862318583f2"
                      },
                      {
                        "type": "@std.button",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Ativar Agora"
                            }
                          },
                          "variant": {
                            "stringVal": {
                              "value": "primary"
                            }
                          },
                          "size": {
                            "stringVal": {
                              "value": "medium"
                            }
                          }
                        },
                        "editorId": "c822dd8f-0da2-453f-8d3c-462eed5fdf11"
                      }
                    ],
                    "editorId": "f6a1eb46-a8e3-421c-a484-1073e30d4b60"
                  }
                ],
                "editorId": "18031358-f7fe-4392-b8c3-7c2044782cbd"
              }
            ],
            "editorId": "00c281b0-7968-4263-8fa1-61359484a203"
          }
        ],
        "editorId": "9e464010-6aeb-43f7-9b4f-82827b2e53a4"
      }
    ],
    "editorId": "ab628781-de45-4e66-b625-0f244577e749"
  }
}
```

### 3. Search Results

- Frame ID: `123e1c4b-edab-4488-bf9c-70b0d1a7b4d0`
- Original page prompt: "A grid-based view showing agents filtered by the user's search query."
- Follow-up prompts: _None_

#### DslDocument (JSON)

```json
{
  "root": {
    "type": "scaffold",
    "properties": {
      "bg": {
        "color": {
          "color": "background"
        }
      }
    },
    "children": [
      {
        "type": "column",
        "properties": {
          "cross_align": {
            "align": {
              "named": "stretch"
            }
          }
        },
        "children": [
          {
            "type": "container",
            "properties": {
              "bg": {
                "color": {
                  "color": "background"
                }
              },
              "padding": {
                "edgeInsets": {
                  "top": 12,
                  "right": 20,
                  "bottom": 12,
                  "left": 20
                }
              },
              "border": {
                "borderSided": {
                  "side": "bottom",
                  "width": 1,
                  "color": "divider"
                }
              }
            },
            "children": [
              {
                "type": "column",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "md"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "space_between"
                        }
                      },
                      "cross_align": {
                        "align": {
                          "named": "center"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "iconbutton",
                        "properties": {
                          "name": {
                            "icon": {
                              "name": "arrow_back_rounded"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "size": {
                            "numberVal": {
                              "value": 24
                            }
                          }
                        },
                        "editorId": "64325021-aea4-447c-8f25-bdfb4e14744a"
                      },
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Busca"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "title_medium"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "font_weight": {
                            "stringVal": {
                              "value": "bold"
                            }
                          }
                        },
                        "editorId": "24e82079-aa98-45cf-986b-f2128a17b1fd"
                      },
                      {
                        "type": "iconbutton",
                        "properties": {
                          "name": {
                            "icon": {
                              "name": "tune_rounded"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "secondary_text"
                            }
                          },
                          "size": {
                            "numberVal": {
                              "value": 20
                            }
                          }
                        },
                        "editorId": "75ee16a5-39ea-4ec8-a69f-1a15b049c048"
                      }
                    ],
                    "editorId": "eb9d6cef-b26d-4732-b37e-85886f7e0e25"
                  },
                  {
                    "type": "@std.textfield",
                    "properties": {
                      "value": {
                        "stringVal": {
                          "value": "Marketing"
                        }
                      },
                      "leading_icon": {
                        "stringVal": {
                          "value": "search_rounded"
                        }
                      },
                      "trailing_icon": {
                        "stringVal": {
                          "value": "close_rounded"
                        }
                      },
                      "variant": {
                        "stringVal": {
                          "value": "filled"
                        }
                      },
                      "bg": {
                        "stringVal": {
                          "value": "surface"
                        }
                      },
                      "radius": {
                        "stringVal": {
                          "value": "lg"
                        }
                      }
                    },
                    "editorId": "42480913-8ea0-4db8-8782-9348c6ec36eb"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "scroll": {
                        "boolVal": {
                          "value": true
                        }
                      },
                      "spacing": {
                        "numberVal": {
                          "value": 0
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "@filter_chip",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Todos"
                            }
                          },
                          "selected": {
                            "boolVal": {
                              "value": true
                            }
                          }
                        },
                        "editorId": "aa3abae7-6125-4aca-8904-16dcc6939332"
                      },
                      {
                        "type": "@filter_chip",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Agentes"
                            }
                          },
                          "selected": {
                            "boolVal": {
                              "value": false
                            }
                          }
                        },
                        "editorId": "f17fe83a-a9bd-49b4-a113-71fe982c7b6b"
                      },
                      {
                        "type": "@filter_chip",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Perfis"
                            }
                          },
                          "selected": {
                            "boolVal": {
                              "value": false
                            }
                          }
                        },
                        "editorId": "352cab44-5dc6-40a4-8c80-1696f9e07c6a"
                      },
                      {
                        "type": "@filter_chip",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Coleções"
                            }
                          },
                          "selected": {
                            "boolVal": {
                              "value": false
                            }
                          }
                        },
                        "editorId": "51f23d77-a604-42e6-bffe-13b2121e3f08"
                      },
                      {
                        "type": "@filter_chip",
                        "properties": {
                          "label": {
                            "stringVal": {
                              "value": "Premium"
                            }
                          },
                          "selected": {
                            "boolVal": {
                              "value": false
                            }
                          }
                        },
                        "editorId": "0f3a3748-e91a-4077-ba58-33e52c077791"
                      }
                    ],
                    "editorId": "a23b3c73-7c0e-4d06-ad68-0cb67e729b29"
                  }
                ],
                "editorId": "6f4f5de5-1b7b-4506-866e-c0d22800132f"
              }
            ],
            "editorId": "8c3f011b-1564-4021-91ff-58869ed04753"
          },
          {
            "type": "expanded",
            "children": [
              {
                "type": "column",
                "properties": {
                  "scroll": {
                    "boolVal": {
                      "value": true
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "lg"
                    }
                  },
                  "spacing": {
                    "stringVal": {
                      "value": "lg"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "stretch"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "space_between"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "12 agentes encontrados"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "label_medium"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "secondary_text"
                            }
                          }
                        },
                        "editorId": "a08ca8d5-8cf5-44e9-b36e-49c40655e95b"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "xs"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Relevância"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              }
                            },
                            "editorId": "9c830aed-f075-456f-9734-e0381276fd8a"
                          },
                          {
                            "type": "icon",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "keyboard_arrow_down_rounded"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              },
                              "size": {
                                "numberVal": {
                                  "value": 16
                                }
                              }
                            },
                            "editorId": "cdf3232a-b87c-4b24-a790-6fa24d79b9e1"
                          }
                        ],
                        "editorId": "ede681cc-cccd-4359-ba18-5a38cb1119ed"
                      }
                    ],
                    "editorId": "a91752a9-564e-4c21-bd2f-c1387fd2771e"
                  },
                  {
                    "type": "column",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "@result_agent_card",
                                "properties": {
                                  "name": {
                                    "stringVal": {
                                      "value": "Social Guru"
                                    }
                                  },
                                  "desc": {
                                    "stringVal": {
                                      "value": "Estrategista de redes sociais viral"
                                    }
                                  },
                                  "img_desc": {
                                    "stringVal": {
                                      "value": "neon social media holographic"
                                    }
                                  },
                                  "rating": {
                                    "stringVal": {
                                      "value": "4.9"
                                    }
                                  },
                                  "category": {
                                    "stringVal": {
                                      "value": "Marketing"
                                    }
                                  }
                                },
                                "editorId": "12791f4b-c1ad-42c0-a98c-7afbf0086f5b"
                              }
                            ],
                            "editorId": "776b6647-2f9f-4906-9d29-74959985d29c"
                          },
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "@result_agent_card",
                                "properties": {
                                  "name": {
                                    "stringVal": {
                                      "value": "Ad Writer"
                                    }
                                  },
                                  "desc": {
                                    "stringVal": {
                                      "value": "Copywriting focado em conversão"
                                    }
                                  },
                                  "img_desc": {
                                    "stringVal": {
                                      "value": "digital typewriter neon"
                                    }
                                  },
                                  "rating": {
                                    "stringVal": {
                                      "value": "4.8"
                                    }
                                  },
                                  "category": {
                                    "stringVal": {
                                      "value": "Ads"
                                    }
                                  }
                                },
                                "editorId": "fab62a4b-17e7-4169-bcbd-044377d7f143"
                              }
                            ],
                            "editorId": "236ea6a8-829d-40d0-81bb-eb650391ca93"
                          }
                        ],
                        "editorId": "c7a0de64-ad4d-416e-81f2-045a6f6a0fb7"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "@result_agent_card",
                                "properties": {
                                  "name": {
                                    "stringVal": {
                                      "value": "Trend Scout"
                                    }
                                  },
                                  "desc": {
                                    "stringVal": {
                                      "value": "Analista de tendências em tempo real"
                                    }
                                  },
                                  "img_desc": {
                                    "stringVal": {
                                      "value": "cyberpunk binoculars"
                                    }
                                  },
                                  "rating": {
                                    "stringVal": {
                                      "value": "4.7"
                                    }
                                  },
                                  "category": {
                                    "stringVal": {
                                      "value": "Research"
                                    }
                                  }
                                },
                                "editorId": "28511fb5-eb7c-4db4-b470-5029719f7dfb"
                              }
                            ],
                            "editorId": "86251929-0097-4cd7-a8fa-a111c9cdf9ed"
                          },
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "@result_agent_card",
                                "properties": {
                                  "name": {
                                    "stringVal": {
                                      "value": "SEO Bot"
                                    }
                                  },
                                  "desc": {
                                    "stringVal": {
                                      "value": "Otimização técnica para buscadores"
                                    }
                                  },
                                  "img_desc": {
                                    "stringVal": {
                                      "value": "matrix code background"
                                    }
                                  },
                                  "rating": {
                                    "stringVal": {
                                      "value": "5.0"
                                    }
                                  },
                                  "category": {
                                    "stringVal": {
                                      "value": "Tech"
                                    }
                                  }
                                },
                                "editorId": "23ff0b5d-2622-4feb-8bde-716ab1851ce7"
                              }
                            ],
                            "editorId": "2bfe432f-2ff2-4816-b0e0-82f64fa1533e"
                          }
                        ],
                        "editorId": "1b138e62-10a4-4739-a14d-dd5d934e8dd7"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "@result_agent_card",
                                "properties": {
                                  "name": {
                                    "stringVal": {
                                      "value": "Brand Voice"
                                    }
                                  },
                                  "desc": {
                                    "stringVal": {
                                      "value": "Criação de identidade verbal única"
                                    }
                                  },
                                  "img_desc": {
                                    "stringVal": {
                                      "value": "abstract vocal waves neon"
                                    }
                                  },
                                  "rating": {
                                    "stringVal": {
                                      "value": "4.6"
                                    }
                                  },
                                  "category": {
                                    "stringVal": {
                                      "value": "Branding"
                                    }
                                  }
                                },
                                "editorId": "f71e4fb4-bdcd-469f-9ac1-e25c4853fbec"
                              }
                            ],
                            "editorId": "58a9abab-7a8a-4a1c-acba-562b67dcd914"
                          },
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "@result_agent_card",
                                "properties": {
                                  "name": {
                                    "stringVal": {
                                      "value": "Mail Magic"
                                    }
                                  },
                                  "desc": {
                                    "stringVal": {
                                      "value": "Automação de e-mail marketing"
                                    }
                                  },
                                  "img_desc": {
                                    "stringVal": {
                                      "value": "glowing envelope icon"
                                    }
                                  },
                                  "rating": {
                                    "stringVal": {
                                      "value": "4.9"
                                    }
                                  },
                                  "category": {
                                    "stringVal": {
                                      "value": "Marketing"
                                    }
                                  }
                                },
                                "editorId": "713e9f6f-138f-423f-ae5a-13fcd24b0276"
                              }
                            ],
                            "editorId": "b0b3fbef-3466-4e7d-a0dc-2e8ec65a3755"
                          }
                        ],
                        "editorId": "3b833676-cf97-49ea-9d8b-be739f258013"
                      }
                    ],
                    "editorId": "3cf8021c-8cf1-4274-80fa-3baa3f1a76b9"
                  },
                  {
                    "type": "container",
                    "properties": {
                      "bg": {
                        "color": {
                          "color": "surface"
                        }
                      },
                      "radius": {
                        "radius": {
                          "topLeft": 0,
                          "topRight": 0,
                          "bottomLeft": 0,
                          "bottomRight": 0,
                          "token": "lg"
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "token": "lg"
                        }
                      },
                      "border": {
                        "border": {
                          "width": 1,
                          "color": "primary/30"
                        }
                      },
                      "margin": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "topToken": "md",
                          "bottomToken": "md"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "column",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          },
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "row",
                            "properties": {
                              "spacing": {
                                "stringVal": {
                                  "value": "sm"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "icon",
                                "properties": {
                                  "name": {
                                    "icon": {
                                      "name": "auto_awesome_rounded"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "on_surface"
                                    }
                                  },
                                  "size": {
                                    "numberVal": {
                                      "value": 24
                                    }
                                  }
                                },
                                "editorId": "e79fe0a7-ae10-432a-aeec-17c8eb3a52aa"
                              },
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "Quer resultados melhores?"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "title_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "primary_text"
                                    }
                                  },
                                  "font_weight": {
                                    "stringVal": {
                                      "value": "bold"
                                    }
                                  }
                                },
                                "editorId": "e170a23c-20d2-4fd7-ba96-3e7d45bc4dcd"
                              }
                            ],
                            "editorId": "dfd3ce9f-ad7d-43af-a0a6-aa09305683c3"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Assine o MuseIA Elite para acessar agentes exclusivos de alta performance."
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "body_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "secondary_text"
                                }
                              }
                            },
                            "editorId": "ed321c33-409b-4c38-a76c-d319a877b383"
                          },
                          {
                            "type": "@std.button",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Ver Planos"
                                }
                              },
                              "variant": {
                                "stringVal": {
                                  "value": "primary"
                                }
                              },
                              "full_width": {
                                "boolVal": {
                                  "value": true
                                }
                              }
                            },
                            "editorId": "1c6c22cf-affa-4911-980d-c5d9e4ff39b9"
                          }
                        ],
                        "editorId": "ae4b0e17-ecd3-4b5a-8901-5e9d36d1dd8f"
                      }
                    ],
                    "editorId": "0b48d08b-b9d0-44c7-b228-d3cec8c7b0b6"
                  },
                  {
                    "type": "column",
                    "properties": {
                      "cross_align": {
                        "align": {
                          "named": "stretch"
                        }
                      },
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Perfis Sugeridos"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "title_medium"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "font_weight": {
                            "stringVal": {
                              "value": "bold"
                            }
                          }
                        },
                        "editorId": "b6392158-9be2-46a6-99c7-c1c865ed586e"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "scroll": {
                            "boolVal": {
                              "value": true
                            }
                          },
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "container",
                            "properties": {
                              "bg": {
                                "color": {
                                  "color": "surface"
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "md"
                                }
                              },
                              "padding": {
                                "edgeInsets": {
                                  "top": 0,
                                  "right": 0,
                                  "bottom": 0,
                                  "left": 0,
                                  "token": "md"
                                }
                              },
                              "width": {
                                "px": {
                                  "value": 140,
                                  "isInfinity": false
                                }
                              },
                              "border": {
                                "border": {
                                  "width": 1,
                                  "color": "divider"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "column",
                                "properties": {
                                  "spacing": {
                                    "stringVal": {
                                      "value": "sm"
                                    }
                                  }
                                },
                                "children": [
                                  {
                                    "type": "avatar",
                                    "properties": {
                                      "source_desc": {
                                        "imageSource": {
                                          "type": "IMAGE_SOURCE_TYPE_URL",
                                          "value": "https://dimg.dreamflow.cloud/v1/image/professional+woman+marketing"
                                        }
                                      },
                                      "size": {
                                        "numberVal": {
                                          "value": 48
                                        }
                                      },
                                      "bg": {
                                        "color": {
                                          "color": "primary",
                                          "opacityPercent": 10
                                        }
                                      }
                                    },
                                    "editorId": "7df07001-2f4d-47fc-a165-e27f5e8ccf8c"
                                  },
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "Agência Alpha"
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "label_large"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "primary_text"
                                        }
                                      },
                                      "max_lines": {
                                        "numberVal": {
                                          "value": 1
                                        }
                                      }
                                    },
                                    "editorId": "fb412dd7-b23a-4ab1-a947-6a8affb8c159"
                                  },
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "5 Agentes"
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "label_small"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "secondary_text"
                                        }
                                      }
                                    },
                                    "editorId": "fd5c0587-4f5f-42f1-88f2-ea2045f7da9c"
                                  }
                                ],
                                "editorId": "f91e1652-54f8-41bf-944f-5ea2be7840f5"
                              }
                            ],
                            "editorId": "cab61e30-4f81-4e95-9a5c-16e4cdfb1351"
                          },
                          {
                            "type": "container",
                            "properties": {
                              "bg": {
                                "color": {
                                  "color": "surface"
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "md"
                                }
                              },
                              "padding": {
                                "edgeInsets": {
                                  "top": 0,
                                  "right": 0,
                                  "bottom": 0,
                                  "left": 0,
                                  "token": "md"
                                }
                              },
                              "width": {
                                "px": {
                                  "value": 140,
                                  "isInfinity": false
                                }
                              },
                              "border": {
                                "border": {
                                  "width": 1,
                                  "color": "divider"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "column",
                                "properties": {
                                  "spacing": {
                                    "stringVal": {
                                      "value": "sm"
                                    }
                                  }
                                },
                                "children": [
                                  {
                                    "type": "avatar",
                                    "properties": {
                                      "source_desc": {
                                        "imageSource": {
                                          "type": "IMAGE_SOURCE_TYPE_URL",
                                          "value": "https://dimg.dreamflow.cloud/v1/image/tech+startup+founder"
                                        }
                                      },
                                      "size": {
                                        "numberVal": {
                                          "value": 48
                                        }
                                      },
                                      "bg": {
                                        "color": {
                                          "color": "accent",
                                          "opacityPercent": 10
                                        }
                                      }
                                    },
                                    "editorId": "f30db488-72a4-4907-8e0b-aa22669042f4"
                                  },
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "Growth Lab"
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "label_large"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "primary_text"
                                        }
                                      },
                                      "max_lines": {
                                        "numberVal": {
                                          "value": 1
                                        }
                                      }
                                    },
                                    "editorId": "b884df35-fb0a-4b1f-a362-1ae8ff74578f"
                                  },
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "12 Agentes"
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "label_small"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "secondary_text"
                                        }
                                      }
                                    },
                                    "editorId": "9e66111f-a58b-4c39-9b57-a684072308c3"
                                  }
                                ],
                                "editorId": "497c7767-61e5-4fb4-9142-34a3867c6fc5"
                              }
                            ],
                            "editorId": "fcf5c42d-605f-43a7-a4cf-c586c2d3be16"
                          },
                          {
                            "type": "container",
                            "properties": {
                              "bg": {
                                "color": {
                                  "color": "surface"
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "md"
                                }
                              },
                              "padding": {
                                "edgeInsets": {
                                  "top": 0,
                                  "right": 0,
                                  "bottom": 0,
                                  "left": 0,
                                  "token": "md"
                                }
                              },
                              "width": {
                                "px": {
                                  "value": 140,
                                  "isInfinity": false
                                }
                              },
                              "border": {
                                "border": {
                                  "width": 1,
                                  "color": "divider"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "column",
                                "properties": {
                                  "spacing": {
                                    "stringVal": {
                                      "value": "sm"
                                    }
                                  }
                                },
                                "children": [
                                  {
                                    "type": "avatar",
                                    "properties": {
                                      "source_desc": {
                                        "imageSource": {
                                          "type": "IMAGE_SOURCE_TYPE_URL",
                                          "value": "https://dimg.dreamflow.cloud/v1/image/creative+designer"
                                        }
                                      },
                                      "size": {
                                        "numberVal": {
                                          "value": 48
                                        }
                                      },
                                      "bg": {
                                        "color": {
                                          "color": "success",
                                          "opacityPercent": 10
                                        }
                                      }
                                    },
                                    "editorId": "98be30f8-a962-4b76-9e7d-ccebe3f97a9f"
                                  },
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "Pixel Perfect"
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "label_large"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "primary_text"
                                        }
                                      },
                                      "max_lines": {
                                        "numberVal": {
                                          "value": 1
                                        }
                                      }
                                    },
                                    "editorId": "4bbca315-c2e6-41c0-be0f-22ecf3897f0e"
                                  },
                                  {
                                    "type": "text",
                                    "properties": {
                                      "content": {
                                        "stringVal": {
                                          "value": "3 Agentes"
                                        }
                                      },
                                      "style": {
                                        "textStyle": {
                                          "styleName": "label_small"
                                        }
                                      },
                                      "color": {
                                        "color": {
                                          "color": "secondary_text"
                                        }
                                      }
                                    },
                                    "editorId": "7a6ab4ce-ee2d-474f-9d72-0b7441258f2a"
                                  }
                                ],
                                "editorId": "f84d9d2d-97b7-43e8-9831-c4b965de1706"
                              }
                            ],
                            "editorId": "3a049897-88c2-4fc5-827e-b4d5362b8260"
                          }
                        ],
                        "editorId": "c3da672c-6d09-440b-b34e-c3a577faa354"
                      }
                    ],
                    "editorId": "e12a177d-731e-4be9-a9c7-21cd23a49408"
                  },
                  {
                    "type": "sizedbox",
                    "properties": {
                      "height": {
                        "stringVal": {
                          "value": "xl"
                        }
                      }
                    },
                    "editorId": "7d58d5f4-b582-4063-ad98-452dbc7babfa"
                  }
                ],
                "editorId": "5f403621-b761-4f5c-ba13-3ec7ecdd6fdc"
              }
            ],
            "editorId": "5f73ee11-d17b-415d-b220-1497f32391d6"
          }
        ],
        "editorId": "d57d7010-e3e3-421a-96cd-bb2614028d14"
      }
    ],
    "editorId": "8fc638e0-d586-4f4e-8fdc-19320f9311e4"
  }
}
```

### 4. Login & Sign Up

- Frame ID: `8055f21b-0a8f-4f4c-8ebe-b5865cc8b00b`
- Original page prompt: "A combined authentication page or modal for user login and registration."
- Follow-up prompts: _None_

#### DslDocument (JSON)

```json
{
  "root": {
    "type": "scaffold",
    "properties": {
      "bg": {
        "color": {
          "color": "background"
        }
      },
      "safe_area": {
        "boolVal": {
          "value": true
        }
      }
    },
    "children": [
      {
        "type": "stack",
        "children": [
          {
            "type": "shader_fill",
            "properties": {
              "preset": {
                "stringVal": {
                  "value": "smokeShade"
                }
              },
              "gradient_angle": {
                "numberVal": {
                  "value": 180
                }
              },
              "color0": {
                "color": {
                  "color": "background"
                }
              },
              "color1": {
                "color": {
                  "color": "surface"
                }
              },
              "color2": {
                "color": {
                  "color": "background"
                }
              },
              "opacity": {
                "numberVal": {
                  "value": 0.4
                }
              }
            },
            "editorId": "c925905c-87be-4aef-9bf1-57267bc078e4"
          },
          {
            "type": "column",
            "properties": {
              "scroll": {
                "boolVal": {
                  "value": true
                }
              },
              "cross_align": {
                "align": {
                  "named": "stretch"
                }
              }
            },
            "children": [
              {
                "type": "container",
                "properties": {
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "lg"
                    }
                  },
                  "height": {
                    "px": {
                      "value": 80,
                      "isInfinity": false
                    }
                  },
                  "align_child": {
                    "align": {
                      "named": "center_left"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "xs"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "logo_icon",
                        "properties": {
                          "name": {
                            "icon": {
                              "name": "openai"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary"
                            }
                          },
                          "size": {
                            "numberVal": {
                              "value": 28
                            }
                          }
                        },
                        "editorId": "2cd8f7b3-c87b-4114-b676-6f2e15dd5556"
                      },
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "MuseIA"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "title_large"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "font_weight": {
                            "numberVal": {
                              "value": 900
                            }
                          },
                          "spacing": {
                            "numberVal": {
                              "value": -1
                            }
                          }
                        },
                        "editorId": "9cb50104-a1f1-48a8-8ff1-9708a7c92a3b"
                      }
                    ],
                    "editorId": "7b91b474-9c4e-484c-af07-7b63fd8c4727"
                  }
                ],
                "editorId": "f7d8a99e-6414-43d1-a2ea-7e55fa6bcccf"
              },
              {
                "type": "column",
                "properties": {
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "topToken": "xl",
                      "rightToken": "lg",
                      "bottomToken": "xl",
                      "leftToken": "lg"
                    }
                  },
                  "spacing": {
                    "stringVal": {
                      "value": "sm"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "start"
                    }
                  }
                },
                "children": [
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Sua jornada com IA começa aqui"
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "headline_medium"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "primary_text"
                        }
                      },
                      "font_weight": {
                        "numberVal": {
                          "value": 800
                        }
                      }
                    },
                    "editorId": "eee6bb5b-1e66-43af-8a6f-b760af0f920a"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Entre para acessar centenas de agentes especializados e turbinar sua produtividade."
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "body_medium"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "secondary_text"
                        }
                      }
                    },
                    "editorId": "af0c4899-f6ef-4689-974a-6444f423864d"
                  }
                ],
                "editorId": "fcf63a68-8630-4ac9-8d03-69e4786c4735"
              },
              {
                "type": "container",
                "properties": {
                  "margin": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "rightToken": "lg",
                      "leftToken": "lg"
                    }
                  },
                  "bg": {
                    "color": {
                      "color": "surface"
                    }
                  },
                  "radius": {
                    "radius": {
                      "topLeft": 0,
                      "topRight": 0,
                      "bottomLeft": 0,
                      "bottomRight": 0,
                      "token": "xl"
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "xl"
                    }
                  },
                  "shadow": {
                    "stringVal": {
                      "value": "xl"
                    }
                  },
                  "border": {
                    "border": {
                      "width": 1,
                      "color": "divider"
                    }
                  }
                },
                "children": [
                  {
                    "type": "column",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "lg"
                        }
                      },
                      "cross_align": {
                        "align": {
                          "named": "stretch"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "numberVal": {
                              "value": 0
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "@auth_tab",
                            "properties": {
                              "label": {
                                "stringVal": {
                                  "value": "Entrar"
                                }
                              },
                              "active": {
                                "boolVal": {
                                  "value": true
                                }
                              }
                            },
                            "editorId": "7a3f8636-6607-4a62-9532-7da687fa11b4"
                          },
                          {
                            "type": "@auth_tab",
                            "properties": {
                              "label": {
                                "stringVal": {
                                  "value": "Cadastrar"
                                }
                              },
                              "active": {
                                "boolVal": {
                                  "value": false
                                }
                              }
                            },
                            "editorId": "44387541-eec0-41bb-bdca-73af8affc35e"
                          }
                        ],
                        "editorId": "6754d3f0-4104-4cab-8c16-392e65f49a3c"
                      },
                      {
                        "type": "sizedbox",
                        "properties": {
                          "height": {
                            "stringVal": {
                              "value": "sm"
                            }
                          }
                        },
                        "editorId": "10cffb45-f600-4164-b786-c0aa54fb8dd7"
                      },
                      {
                        "type": "column",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "column",
                            "properties": {
                              "spacing": {
                                "stringVal": {
                                  "value": "xs"
                                }
                              },
                              "cross_align": {
                                "align": {
                                  "named": "start"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "E-mail"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "label_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "secondary_text"
                                    }
                                  },
                                  "margin": {
                                    "edgeInsets": {
                                      "top": 0,
                                      "right": 0,
                                      "bottom": 0,
                                      "left": 4
                                    }
                                  }
                                },
                                "editorId": "c3d98ddc-282e-42e8-afc7-46647c529ce0"
                              },
                              {
                                "type": "@std.textfield",
                                "properties": {
                                  "hint": {
                                    "stringVal": {
                                      "value": "seu@email.com"
                                    }
                                  },
                                  "leading_icon": {
                                    "stringVal": {
                                      "value": "mail_outline_rounded"
                                    }
                                  },
                                  "variant": {
                                    "stringVal": {
                                      "value": "filled"
                                    }
                                  },
                                  "bg": {
                                    "stringVal": {
                                      "value": "background"
                                    }
                                  }
                                },
                                "editorId": "10253590-ff40-4b28-b660-8b4112796f2c"
                              }
                            ],
                            "editorId": "a0847845-a28d-4121-8695-45c4044c1b19"
                          },
                          {
                            "type": "column",
                            "properties": {
                              "spacing": {
                                "stringVal": {
                                  "value": "xs"
                                }
                              },
                              "cross_align": {
                                "align": {
                                  "named": "start"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "Senha"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "label_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "secondary_text"
                                    }
                                  },
                                  "margin": {
                                    "edgeInsets": {
                                      "top": 0,
                                      "right": 0,
                                      "bottom": 0,
                                      "left": 4
                                    }
                                  }
                                },
                                "editorId": "d331acf8-6fc7-49aa-8b96-056b580a53d4"
                              },
                              {
                                "type": "@std.textfield",
                                "properties": {
                                  "hint": {
                                    "stringVal": {
                                      "value": "••••••••"
                                    }
                                  },
                                  "leading_icon": {
                                    "stringVal": {
                                      "value": "lock_outline_rounded"
                                    }
                                  },
                                  "trailing_icon": {
                                    "stringVal": {
                                      "value": "visibility_off_rounded"
                                    }
                                  },
                                  "variant": {
                                    "stringVal": {
                                      "value": "filled"
                                    }
                                  },
                                  "bg": {
                                    "stringVal": {
                                      "value": "background"
                                    }
                                  }
                                },
                                "editorId": "b8e0f5c3-e1dd-4fdf-9ca2-9bcec5a684d5"
                              }
                            ],
                            "editorId": "2577f06c-e066-4924-a5b8-81af3766a2ea"
                          }
                        ],
                        "editorId": "9842b48e-158b-4bd0-8d07-94cf4fdfa6fb"
                      },
                      {
                        "type": "container",
                        "properties": {
                          "align": {
                            "align": {
                              "named": "center_right"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "@std.button",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Esqueceu a senha?"
                                }
                              },
                              "variant": {
                                "stringVal": {
                                  "value": "ghost"
                                }
                              },
                              "size": {
                                "stringVal": {
                                  "value": "small"
                                }
                              }
                            },
                            "editorId": "f2268f9f-e360-4641-9b2a-4b8e5c9f67dd"
                          }
                        ],
                        "editorId": "5954459d-989f-411a-97cf-8ca9bcf32e93"
                      },
                      {
                        "type": "@std.button",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Entrar na Plataforma"
                            }
                          },
                          "variant": {
                            "stringVal": {
                              "value": "primary"
                            }
                          },
                          "size": {
                            "stringVal": {
                              "value": "large"
                            }
                          },
                          "full_width": {
                            "boolVal": {
                              "value": true
                            }
                          }
                        },
                        "editorId": "164a3dcf-64c8-472a-9536-ac7d52882dd3"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          },
                          "align": {
                            "align": {
                              "named": "center"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "divider",
                                "properties": {
                                  "color": {
                                    "color": {
                                      "color": "divider"
                                    }
                                  },
                                  "thickness": {
                                    "numberVal": {
                                      "value": 1
                                    }
                                  }
                                },
                                "editorId": "d7365595-5669-4d0e-99f4-7df49c22e146"
                              }
                            ],
                            "editorId": "46c199b4-1fa3-405e-8983-e1157bc5ae07"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "OU"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_surface"
                                }
                              }
                            },
                            "editorId": "69ced123-69d6-4849-bbd4-b815e2e3b380"
                          },
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "divider",
                                "properties": {
                                  "color": {
                                    "color": {
                                      "color": "divider"
                                    }
                                  },
                                  "thickness": {
                                    "numberVal": {
                                      "value": 1
                                    }
                                  }
                                },
                                "editorId": "4aba6cfd-95fa-47b8-a333-5a34d9302b8c"
                              }
                            ],
                            "editorId": "79674bcd-2a00-41f1-814e-811ed9bbb0f1"
                          }
                        ],
                        "editorId": "7e077f7a-be83-432a-9483-0d5a2dc16ead"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "@social_button",
                            "properties": {
                              "icon": {
                                "stringVal": {
                                  "value": "google"
                                }
                              },
                              "label": {
                                "stringVal": {
                                  "value": "Google"
                                }
                              }
                            },
                            "editorId": "c2a1176d-70dd-4588-815c-d13b9fac71e3"
                          },
                          {
                            "type": "@social_button",
                            "properties": {
                              "icon": {
                                "stringVal": {
                                  "value": "apple"
                                }
                              },
                              "label": {
                                "stringVal": {
                                  "value": "Apple"
                                }
                              }
                            },
                            "editorId": "eb650c8b-987c-469c-92a7-3e63c1d8eef1"
                          }
                        ],
                        "editorId": "290125d6-08ea-4fb9-ba88-5ec29471bc33"
                      }
                    ],
                    "editorId": "47ea47d1-08e8-406b-a098-a94e13094d6c"
                  }
                ],
                "editorId": "235bad5a-a9c3-4b2b-96e0-bda0680854b2"
              },
              {
                "type": "column",
                "properties": {
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "xl"
                    }
                  },
                  "spacing": {
                    "stringVal": {
                      "value": "lg"
                    }
                  },
                  "align": {
                    "align": {
                      "named": "center"
                    }
                  }
                },
                "children": [
                  {
                    "type": "container",
                    "properties": {
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "token": "md"
                        }
                      },
                      "radius": {
                        "radius": {
                          "topLeft": 0,
                          "topRight": 0,
                          "bottomLeft": 0,
                          "bottomRight": 0,
                          "token": "lg"
                        }
                      },
                      "bg": {
                        "color": {
                          "color": "primary",
                          "opacityPercent": 10
                        }
                      },
                      "border": {
                        "border": {
                          "width": 1,
                          "color": "primary/20"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "md"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "icon",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "auto_awesome_rounded"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              },
                              "size": {
                                "numberVal": {
                                  "value": 20
                                }
                              }
                            },
                            "editorId": "18cdda57-4193-488c-ab4c-d2b7a616e368"
                          },
                          {
                            "type": "expanded",
                            "children": [
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "Assine o MuseIA Elite e tenha acesso ilimitado a todos os agentes por 30 dias."
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "body_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "primary_text"
                                    }
                                  }
                                },
                                "editorId": "43c4abcb-59e5-4c9a-81ff-f011ee5d83bc"
                              }
                            ],
                            "editorId": "e4cc6531-35de-401f-9489-fce0706285b3"
                          }
                        ],
                        "editorId": "3ddc1ec4-8928-4da5-8c3c-21ead778ebe1"
                      }
                    ],
                    "editorId": "354c5ed7-b03c-498b-92d8-b1ae4de3677d"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "xs"
                        }
                      },
                      "align": {
                        "align": {
                          "named": "center"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Ainda não tem uma conta?"
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "body_small"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "secondary_text"
                            }
                          }
                        },
                        "editorId": "57af441d-ad67-4836-bf5c-98a1b98a130d"
                      },
                      {
                        "type": "@std.button",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Criar agora"
                            }
                          },
                          "variant": {
                            "stringVal": {
                              "value": "ghost"
                            }
                          },
                          "size": {
                            "stringVal": {
                              "value": "small"
                            }
                          }
                        },
                        "editorId": "89e1988c-07c0-46e6-93db-0b59f61c495f"
                      }
                    ],
                    "editorId": "162aca60-06cb-40c4-9956-33377a636554"
                  }
                ],
                "editorId": "c1f4f0b6-6a4b-4249-9ff9-63905e26be47"
              },
              {
                "type": "sizedbox",
                "properties": {
                  "height": {
                    "stringVal": {
                      "value": "xl"
                    }
                  }
                },
                "editorId": "6e39c0ab-3aa7-4c43-ba3e-753e5b37242c"
              }
            ],
            "editorId": "d2a61496-6801-4ff6-b96c-684470f7f4be"
          },
          {
            "type": "container",
            "properties": {
              "align": {
                "align": {
                  "named": "top_left"
                }
              },
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "token": "lg"
                }
              }
            },
            "children": [
              {
                "type": "iconbutton",
                "properties": {
                  "name": {
                    "icon": {
                      "name": "arrow_back_rounded"
                    }
                  },
                  "bg": {
                    "color": {
                      "color": "surface",
                      "opacityPercent": 50
                    }
                  },
                  "color": {
                    "color": {
                      "color": "primary_text"
                    }
                  },
                  "radius": {
                    "radius": {
                      "topLeft": 0,
                      "topRight": 0,
                      "bottomLeft": 0,
                      "bottomRight": 0,
                      "token": "full"
                    }
                  },
                  "backdrop_blur": {
                    "numberVal": {
                      "value": 10
                    }
                  }
                },
                "editorId": "8a444b04-c78d-4862-ae93-3dbfdf2c6bbf"
              }
            ],
            "editorId": "071fdfb2-a0ab-4aff-8b82-64663a03e936"
          }
        ],
        "editorId": "967add71-00d0-40f0-aafd-8695fcd6bbe2"
      }
    ],
    "editorId": "895ec290-98f5-4629-9fe3-ef7deb48dcfb"
  }
}
```

### 5. Subscription & Payment

- Frame ID: `7cac7f95-b11b-41e4-8b0f-a5b26a42304b`
- Original page prompt: "A conversion-focused page showing access plans, 30-day access benefits, and payment methods."
- Follow-up prompts: _None_

#### DslDocument (JSON)

```json
{
  "root": {
    "type": "scaffold",
    "properties": {
      "bg": {
        "color": {
          "color": "background"
        }
      },
      "safe_area": {
        "boolVal": {
          "value": true
        }
      }
    },
    "children": [
      {
        "type": "column",
        "properties": {
          "scroll": {
            "boolVal": {
              "value": true
            }
          },
          "cross_align": {
            "align": {
              "named": "stretch"
            }
          }
        },
        "children": [
          {
            "type": "container",
            "properties": {
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "topToken": "md",
                  "rightToken": "lg",
                  "bottomToken": "md",
                  "leftToken": "lg"
                }
              },
              "border": {
                "borderSided": {
                  "side": "bottom",
                  "width": 1,
                  "color": "divider"
                }
              }
            },
            "children": [
              {
                "type": "row",
                "properties": {
                  "align": {
                    "align": {
                      "named": "space_between"
                    }
                  }
                },
                "children": [
                  {
                    "type": "iconbutton",
                    "properties": {
                      "name": {
                        "icon": {
                          "name": "close_rounded"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "primary_text"
                        }
                      },
                      "size": {
                        "numberVal": {
                          "value": 24
                        }
                      }
                    },
                    "editorId": "4889ad2f-9079-4f11-a8cb-e6e132804347"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Ativar Acesso"
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "title_medium"
                        }
                      },
                      "font_weight": {
                        "stringVal": {
                          "value": "bold"
                        }
                      }
                    },
                    "editorId": "bfffec96-a568-47f4-8861-082b0d2e49ce"
                  },
                  {
                    "type": "sizedbox",
                    "properties": {
                      "width": {
                        "px": {
                          "value": 40,
                          "isInfinity": false
                        }
                      }
                    },
                    "editorId": "ef223284-56b1-4e77-b301-c243f96cd54e"
                  }
                ],
                "editorId": "23ee9723-f873-431c-a5fa-2e97b9661e85"
              }
            ],
            "editorId": "ee8cd4da-58ab-407f-ba51-2ae20b404c57"
          },
          {
            "type": "container",
            "properties": {
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "topToken": "xl",
                  "rightToken": "lg",
                  "bottomToken": "xl",
                  "leftToken": "lg"
                }
              },
              "gradient": {
                "gradient": {
                  "type": "GRADIENT_TYPE_LINEAR",
                  "direction": "to_bottom",
                  "stops": [
                    {
                      "color": "primary/10"
                    },
                    {
                      "color": "background"
                    }
                  ]
                }
              }
            },
            "children": [
              {
                "type": "column",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "md"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "center"
                    }
                  }
                },
                "children": [
                  {
                    "type": "container",
                    "properties": {
                      "bg": {
                        "color": {
                          "color": "primary",
                          "opacityPercent": 20
                        }
                      },
                      "padding": {
                        "edgeInsets": {
                          "top": 0,
                          "right": 0,
                          "bottom": 0,
                          "left": 0,
                          "topToken": "sm",
                          "rightToken": "md",
                          "bottomToken": "sm",
                          "leftToken": "md"
                        }
                      },
                      "radius": {
                        "radius": {
                          "topLeft": 0,
                          "topRight": 0,
                          "bottomLeft": 0,
                          "bottomRight": 0,
                          "token": "full"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "row",
                        "properties": {
                          "main_size": {
                            "stringVal": {
                              "value": "min"
                            }
                          },
                          "spacing": {
                            "stringVal": {
                              "value": "xs"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "icon",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "auto_awesome_rounded"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              },
                              "size": {
                                "numberVal": {
                                  "value": 16
                                }
                              }
                            },
                            "editorId": "f0621ae5-2bd6-4cbf-984c-916b0e7e616b"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "MUSEIA ELITE"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "label_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              },
                              "font_weight": {
                                "stringVal": {
                                  "value": "bold"
                                }
                              }
                            },
                            "editorId": "db7544e6-8b46-4942-bb78-7940ecc2493a"
                          }
                        ],
                        "editorId": "85dd2fe5-0f61-4196-a7f7-6676081790f5"
                      }
                    ],
                    "editorId": "c64c2158-f951-4e0d-bd5f-822cdda8a82c"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Passe de Acesso 30 Dias"
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "headline_medium"
                        }
                      },
                      "text_align": {
                        "align": {
                          "named": "center"
                        }
                      },
                      "font_weight": {
                        "numberVal": {
                          "value": 900
                        }
                      },
                      "color": {
                        "color": {
                          "color": "primary_text"
                        }
                      }
                    },
                    "editorId": "e614ae0f-1f8b-4096-b871-f1b1ff45f4e8"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Desbloqueie o poder total de todos os agentes de IA sem limites."
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "body_large"
                        }
                      },
                      "text_align": {
                        "align": {
                          "named": "center"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "secondary_text"
                        }
                      }
                    },
                    "editorId": "58c3305e-8fe3-40ec-b60b-8403311bc874"
                  }
                ],
                "editorId": "1866751a-6c59-48fb-a459-cfa05be2cef4"
              }
            ],
            "editorId": "60d5a6aa-8739-46ec-b555-b57a1834b5a0"
          },
          {
            "type": "column",
            "properties": {
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "rightToken": "lg",
                  "leftToken": "lg"
                }
              },
              "cross_align": {
                "align": {
                  "named": "stretch"
                }
              }
            },
            "children": [
              {
                "type": "container",
                "properties": {
                  "bg": {
                    "color": {
                      "color": "surface"
                    }
                  },
                  "radius": {
                    "radius": {
                      "topLeft": 0,
                      "topRight": 0,
                      "bottomLeft": 0,
                      "bottomRight": 0,
                      "token": "xl"
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "xl"
                    }
                  },
                  "border": {
                    "border": {
                      "width": 1,
                      "color": "divider"
                    }
                  },
                  "shadow": {
                    "stringVal": {
                      "value": "sm"
                    }
                  }
                },
                "children": [
                  {
                    "type": "column",
                    "properties": {
                      "cross_align": {
                        "align": {
                          "named": "stretch"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "@benefit_item__da4160a0",
                        "properties": {
                          "text": {
                            "stringVal": {
                              "value": "Acesso ilimitado a +50 agentes premium"
                            }
                          }
                        },
                        "editorId": "86bc1b3d-bfdb-410c-891c-eb4847fb0831"
                      },
                      {
                        "type": "@benefit_item__da4160a0",
                        "properties": {
                          "text": {
                            "stringVal": {
                              "value": "Processamento prioritário (sem filas)"
                            }
                          }
                        },
                        "editorId": "ac6b4a52-7acd-440d-9df3-6db6eeb975f3"
                      },
                      {
                        "type": "@benefit_item__da4160a0",
                        "properties": {
                          "text": {
                            "stringVal": {
                              "value": "Suporte a arquivos e documentos complexos"
                            }
                          }
                        },
                        "editorId": "b02492ae-1c31-4b9d-b497-e8b32a8ab0c1"
                      },
                      {
                        "type": "@benefit_item__da4160a0",
                        "properties": {
                          "text": {
                            "stringVal": {
                              "value": "Geração de imagens em alta resolução"
                            }
                          }
                        },
                        "editorId": "ec73cf2f-8922-4fee-b018-9ebb424f72ba"
                      },
                      {
                        "type": "@benefit_item__da4160a0",
                        "properties": {
                          "text": {
                            "stringVal": {
                              "value": "Histórico de conversas salvo na nuvem"
                            }
                          }
                        },
                        "editorId": "65b36fdf-9206-4237-8ee3-e6c77662e9a5"
                      },
                      {
                        "type": "divider",
                        "properties": {
                          "color": {
                            "color": {
                              "color": "divider"
                            }
                          },
                          "margin": {
                            "edgeInsets": {
                              "top": 0,
                              "right": 0,
                              "bottom": 0,
                              "left": 0,
                              "topToken": "md",
                              "bottomToken": "lg"
                            }
                          }
                        },
                        "editorId": "f365d218-c6b0-493b-952b-0abd87aded61"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "align": {
                            "align": {
                              "named": "space_between"
                            }
                          },
                          "cross_align": {
                            "align": {
                              "named": "center"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "column",
                            "properties": {
                              "cross_align": {
                                "align": {
                                  "named": "start"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "Pagamento único"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "label_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "secondary_text"
                                    }
                                  }
                                },
                                "editorId": "dcfee056-b356-4f90-b355-c57945e88177"
                              },
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "R$ 49,90"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "headline_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "primary_text"
                                    }
                                  },
                                  "font_weight": {
                                    "numberVal": {
                                      "value": 800
                                    }
                                  }
                                },
                                "editorId": "293233ca-5bc2-4201-ba90-bc9864d67055"
                              }
                            ],
                            "editorId": "f835b759-674f-43e0-a05f-97f99da040fe"
                          },
                          {
                            "type": "container",
                            "properties": {
                              "bg": {
                                "color": {
                                  "color": "success"
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "md"
                                }
                              },
                              "padding": {
                                "edgeInsets": {
                                  "top": 0,
                                  "right": 0,
                                  "bottom": 0,
                                  "left": 0,
                                  "topToken": "sm",
                                  "rightToken": "md",
                                  "bottomToken": "sm",
                                  "leftToken": "md"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "MELHOR VALOR"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "label_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "on_secondary"
                                    }
                                  },
                                  "font_weight": {
                                    "stringVal": {
                                      "value": "bold"
                                    }
                                  }
                                },
                                "editorId": "eef573ec-9a78-4322-b1d1-f22d9df669cd"
                              }
                            ],
                            "editorId": "cff7bcf8-ad0d-468c-be65-2ff988199277"
                          }
                        ],
                        "editorId": "e4a7029f-51e0-40d8-80e6-a53d25f9655c"
                      }
                    ],
                    "editorId": "c01e0995-64c4-403c-a4c2-f753c6e1c490"
                  }
                ],
                "editorId": "46b43c90-a922-4891-bd57-e88d17ed90af"
              }
            ],
            "editorId": "497b359c-3c60-438d-95e2-44d21d328fab"
          },
          {
            "type": "column",
            "properties": {
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "topToken": "xl",
                  "rightToken": "lg",
                  "bottomToken": "xl",
                  "leftToken": "lg"
                }
              },
              "cross_align": {
                "align": {
                  "named": "stretch"
                }
              }
            },
            "children": [
              {
                "type": "text",
                "properties": {
                  "content": {
                    "stringVal": {
                      "value": "Escolha a forma de pagamento"
                    }
                  },
                  "style": {
                    "textStyle": {
                      "styleName": "title_medium"
                    }
                  },
                  "color": {
                    "color": {
                      "color": "primary_text"
                    }
                  },
                  "font_weight": {
                    "stringVal": {
                      "value": "bold"
                    }
                  },
                  "margin": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "bottomToken": "lg"
                    }
                  }
                },
                "editorId": "062094bd-f875-4189-a560-21b1692265ed"
              },
              {
                "type": "@payment_option",
                "properties": {
                  "icon": {
                    "stringVal": {
                      "value": "pix_rounded"
                    }
                  },
                  "title": {
                    "stringVal": {
                      "value": "Pix"
                    }
                  },
                  "subtitle": {
                    "stringVal": {
                      "value": "Aprovação instantânea"
                    }
                  },
                  "selected": {
                    "boolVal": {
                      "value": true
                    }
                  }
                },
                "editorId": "8dec0644-8e7f-4047-8ca4-f32180580cfd"
              },
              {
                "type": "@payment_option",
                "properties": {
                  "icon": {
                    "stringVal": {
                      "value": "credit_card_rounded"
                    }
                  },
                  "title": {
                    "stringVal": {
                      "value": "Cartão de Crédito"
                    }
                  },
                  "subtitle": {
                    "stringVal": {
                      "value": "Até 12x com juros"
                    }
                  },
                  "selected": {
                    "boolVal": {
                      "value": false
                    }
                  }
                },
                "editorId": "10d87b80-d8e7-4312-af27-49f80cb0068f"
              },
              {
                "type": "@payment_option",
                "properties": {
                  "icon": {
                    "stringVal": {
                      "value": "account_balance_wallet_rounded"
                    }
                  },
                  "title": {
                    "stringVal": {
                      "value": "Google Pay"
                    }
                  },
                  "subtitle": {
                    "stringVal": {
                      "value": "Rápido e seguro"
                    }
                  },
                  "selected": {
                    "boolVal": {
                      "value": false
                    }
                  }
                },
                "editorId": "d408f249-af37-42a7-873f-89b77ae45480"
              }
            ],
            "editorId": "af4b8cd7-52b5-47db-b43d-7928babdc9d1"
          },
          {
            "type": "container",
            "properties": {
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "token": "lg"
                }
              },
              "margin": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "rightToken": "lg",
                  "bottomToken": "xl",
                  "leftToken": "lg"
                }
              },
              "radius": {
                "radius": {
                  "topLeft": 0,
                  "topRight": 0,
                  "bottomLeft": 0,
                  "bottomRight": 0,
                  "token": "lg"
                }
              },
              "bg": {
                "color": {
                  "color": "surface",
                  "opacityPercent": 50
                }
              },
              "border": {
                "border": {
                  "width": 1,
                  "color": "divider"
                }
              }
            },
            "children": [
              {
                "type": "row",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "md"
                    }
                  }
                },
                "children": [
                  {
                    "type": "icon",
                    "properties": {
                      "name": {
                        "icon": {
                          "name": "security_rounded"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "secondary_text"
                        }
                      },
                      "size": {
                        "numberVal": {
                          "value": 20
                        }
                      }
                    },
                    "editorId": "0c9bd90d-8abd-46be-808a-35d5578ed5e4"
                  },
                  {
                    "type": "expanded",
                    "children": [
                      {
                        "type": "text",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Pagamento processado em ambiente seguro e criptografado."
                            }
                          },
                          "style": {
                            "textStyle": {
                              "styleName": "body_small"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "secondary_text"
                            }
                          }
                        },
                        "editorId": "721abd02-96b9-414c-b7c6-5c6c65a2ac25"
                      }
                    ],
                    "editorId": "63142956-0c95-4098-9597-6d0f496a3284"
                  }
                ],
                "editorId": "a5cfc9fb-c7fc-47bc-a618-fe5acf6024a3"
              }
            ],
            "editorId": "c9fd23fa-e3cf-4fa8-8ab1-4a8a2c886de7"
          },
          {
            "type": "container",
            "properties": {
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "token": "lg"
                }
              },
              "bg": {
                "color": {
                  "color": "surface"
                }
              },
              "border": {
                "borderSided": {
                  "side": "top",
                  "width": 1,
                  "color": "divider"
                }
              }
            },
            "children": [
              {
                "type": "column",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "md"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "stretch"
                    }
                  }
                },
                "children": [
                  {
                    "type": "@std.button",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Finalizar Pagamento"
                        }
                      },
                      "variant": {
                        "stringVal": {
                          "value": "primary"
                        }
                      },
                      "size": {
                        "stringVal": {
                          "value": "large"
                        }
                      },
                      "full_width": {
                        "boolVal": {
                          "value": true
                        }
                      }
                    },
                    "editorId": "408a2dd9-0ab6-48a3-aab4-1105c55e135b"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Ao prosseguir, você concorda com nossos Termos de Uso."
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "label_small"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "on_surface"
                        }
                      },
                      "text_align": {
                        "align": {
                          "named": "center"
                        }
                      }
                    },
                    "editorId": "de029d88-ebcc-4a7f-8a44-f6e7e83fafc1"
                  }
                ],
                "editorId": "7069124c-47b1-4d20-978d-f9e7e2a40691"
              }
            ],
            "editorId": "3270bfe9-f1fc-4f1e-a8b7-fb409980f90e"
          },
          {
            "type": "sizedbox",
            "properties": {
              "height": {
                "stringVal": {
                  "value": "lg"
                }
              }
            },
            "editorId": "40641061-abd5-4065-9c8f-600ebcc5be42"
          }
        ],
        "editorId": "dfce9260-95bc-4201-a5ee-7d6173553e61"
      }
    ],
    "editorId": "0b4a300b-a7e0-47ba-a1d2-c778900cc287"
  }
}
```

### 6. User Profile

- Frame ID: `886a7a51-3eac-4de4-a23c-99aec1fe3a59`
- Original page prompt: "A dashboard for the user to see their active access status and history of used agents."
- Follow-up prompts: _None_

#### DslDocument (JSON)

```json
{
  "root": {
    "type": "scaffold",
    "properties": {
      "bg": {
        "color": {
          "color": "background"
        }
      }
    },
    "children": [
      {
        "type": "column",
        "properties": {
          "scroll": {
            "boolVal": {
              "value": true
            }
          },
          "cross_align": {
            "align": {
              "named": "stretch"
            }
          }
        },
        "children": [
          {
            "type": "stack",
            "children": [
              {
                "type": "container",
                "properties": {
                  "height": {
                    "px": {
                      "value": 220,
                      "isInfinity": false
                    }
                  },
                  "width": {
                    "px": {
                      "value": "Infinity",
                      "isInfinity": true
                    }
                  },
                  "clip": {
                    "boolVal": {
                      "value": true
                    }
                  }
                },
                "children": [
                  {
                    "type": "image",
                    "properties": {
                      "source_desc": {
                        "imageSource": {
                          "type": "IMAGE_SOURCE_TYPE_URL",
                          "value": "https://dimg.dreamflow.cloud/v1/image/abstract+dark+purple+fluid+background"
                        }
                      },
                      "fit": {
                        "stringVal": {
                          "value": "cover"
                        }
                      }
                    },
                    "editorId": "8526c2d1-0c7b-4f95-b4ed-a9ad8864671c"
                  }
                ],
                "editorId": "55358793-9452-4ab9-a4a1-de07cf23dac6"
              },
              {
                "type": "container",
                "properties": {
                  "gradient": {
                    "gradient": {
                      "type": "GRADIENT_TYPE_LINEAR",
                      "direction": "to_top",
                      "stops": [
                        {
                          "color": "background",
                          "position": 0
                        },
                        {
                          "color": "background/20",
                          "position": 100
                        }
                      ]
                    }
                  }
                },
                "editorId": "14f568bd-efd1-46a9-9217-f30c499acfae"
              },
              {
                "type": "column",
                "properties": {
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "rightToken": "lg",
                      "leftToken": "lg"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "start"
                    }
                  }
                },
                "children": [
                  {
                    "type": "sizedbox",
                    "properties": {
                      "height": {
                        "px": {
                          "value": 60,
                          "isInfinity": false
                        }
                      }
                    },
                    "editorId": "65f9f0a0-fbfd-4a4e-86d7-9692e0473e25"
                  },
                  {
                    "type": "row",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "space_between"
                        }
                      },
                      "cross_align": {
                        "align": {
                          "named": "end"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "container",
                        "properties": {
                          "width": {
                            "px": {
                              "value": 100,
                              "isInfinity": false
                            }
                          },
                          "height": {
                            "px": {
                              "value": 100,
                              "isInfinity": false
                            }
                          },
                          "radius": {
                            "radius": {
                              "topLeft": 0,
                              "topRight": 0,
                              "bottomLeft": 0,
                              "bottomRight": 0,
                              "token": "full"
                            }
                          },
                          "border": {
                            "border": {
                              "width": 4,
                              "color": "background"
                            }
                          },
                          "clip": {
                            "boolVal": {
                              "value": true
                            }
                          },
                          "shadow": {
                            "stringVal": {
                              "value": "lg"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "image",
                            "properties": {
                              "source_desc": {
                                "imageSource": {
                                  "type": "IMAGE_SOURCE_TYPE_URL",
                                  "value": "https://dimg.dreamflow.cloud/v1/image/modern+stylish+person+portrait"
                                }
                              },
                              "fit": {
                                "stringVal": {
                                  "value": "cover"
                                }
                              }
                            },
                            "editorId": "6ab14eb2-99ed-494d-af08-8e047365d1af"
                          }
                        ],
                        "editorId": "e1fd5ec3-1ea4-4f38-9d54-b1dedd926a55"
                      },
                      {
                        "type": "@std.button",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Editar Perfil"
                            }
                          },
                          "variant": {
                            "stringVal": {
                              "value": "outline"
                            }
                          },
                          "size": {
                            "stringVal": {
                              "value": "small"
                            }
                          }
                        },
                        "editorId": "a10aea50-eef1-4779-9008-6745dcd1c82d"
                      }
                    ],
                    "editorId": "a85ab046-04c9-4354-afe0-7dacf63468d1"
                  },
                  {
                    "type": "sizedbox",
                    "properties": {
                      "height": {
                        "stringVal": {
                          "value": "md"
                        }
                      }
                    },
                    "editorId": "543f12a7-a7dc-4edd-98e0-c3e76af994ae"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Alex Silva"
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "headline_small"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "primary_text"
                        }
                      },
                      "font_weight": {
                        "numberVal": {
                          "value": 800
                        }
                      }
                    },
                    "editorId": "5b94914b-7a3f-46b7-915b-c8903e5fd4f3"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Membro MuseIA desde Out 2023"
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "body_small"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "secondary_text"
                        }
                      }
                    },
                    "editorId": "85f1f428-946f-4d34-8536-e6abca7d8c75"
                  }
                ],
                "editorId": "88decd1e-9eb0-490a-bbf8-1f63cb2e0494"
              }
            ],
            "editorId": "bb801477-6dec-4abf-8dcf-1df6fcc4772a"
          },
          {
            "type": "column",
            "properties": {
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "token": "lg"
                }
              },
              "spacing": {
                "stringVal": {
                  "value": "md"
                }
              }
            },
            "children": [
              {
                "type": "container",
                "properties": {
                  "bg": {
                    "color": {
                      "color": "surface"
                    }
                  },
                  "radius": {
                    "radius": {
                      "topLeft": 0,
                      "topRight": 0,
                      "bottomLeft": 0,
                      "bottomRight": 0,
                      "token": "xl"
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "token": "lg"
                    }
                  },
                  "border": {
                    "border": {
                      "width": 1,
                      "color": "primary/30"
                    }
                  },
                  "shadow": {
                    "stringVal": {
                      "value": "md"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "spacing": {
                        "stringVal": {
                          "value": "md"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "container",
                        "properties": {
                          "width": {
                            "px": {
                              "value": 48,
                              "isInfinity": false
                            }
                          },
                          "height": {
                            "px": {
                              "value": 48,
                              "isInfinity": false
                            }
                          },
                          "bg": {
                            "color": {
                              "color": "primary",
                              "opacityPercent": 10
                            }
                          },
                          "radius": {
                            "radius": {
                              "topLeft": 0,
                              "topRight": 0,
                              "bottomLeft": 0,
                              "bottomRight": 0,
                              "token": "full"
                            }
                          },
                          "align_child": {
                            "align": {
                              "named": "center"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "icon",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "diamond_rounded"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "on_primary"
                                }
                              },
                              "size": {
                                "numberVal": {
                                  "value": 28
                                }
                              }
                            },
                            "editorId": "7a3dcdc6-6722-4651-9e4a-b24b118d8723"
                          }
                        ],
                        "editorId": "b335afec-9f28-4104-ad60-ba7f46075014"
                      },
                      {
                        "type": "expanded",
                        "children": [
                          {
                            "type": "column",
                            "properties": {
                              "cross_align": {
                                "align": {
                                  "named": "start"
                                }
                              },
                              "spacing": {
                                "stringVal": {
                                  "value": "xs"
                                }
                              }
                            },
                            "children": [
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "Plano Pro Ativo"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "title_medium"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "primary_text"
                                    }
                                  },
                                  "font_weight": {
                                    "stringVal": {
                                      "value": "bold"
                                    }
                                  }
                                },
                                "editorId": "78ee2041-db10-4088-ac13-44900521db1a"
                              },
                              {
                                "type": "text",
                                "properties": {
                                  "content": {
                                    "stringVal": {
                                      "value": "Sua assinatura renova em 12 dias"
                                    }
                                  },
                                  "style": {
                                    "textStyle": {
                                      "styleName": "body_small"
                                    }
                                  },
                                  "color": {
                                    "color": {
                                      "color": "secondary_text"
                                    }
                                  }
                                },
                                "editorId": "9c1e1759-fe77-418a-9bdc-1761302ff806"
                              }
                            ],
                            "editorId": "db4031b2-5ea9-4d3a-888d-dac2755becc8"
                          }
                        ],
                        "editorId": "c219af4d-a45a-45d2-b00c-79a650503e29"
                      },
                      {
                        "type": "@std.button",
                        "properties": {
                          "content": {
                            "stringVal": {
                              "value": "Gerenciar"
                            }
                          },
                          "variant": {
                            "stringVal": {
                              "value": "ghost"
                            }
                          },
                          "size": {
                            "stringVal": {
                              "value": "small"
                            }
                          },
                          "color": {
                            "stringVal": {
                              "value": "primary"
                            }
                          }
                        },
                        "editorId": "398fb86c-1a73-4c0a-9c6a-cc92210277f3"
                      }
                    ],
                    "editorId": "785d6d24-cbb2-4805-a7ab-a6c030173e9d"
                  }
                ],
                "editorId": "b978001c-7877-43b9-82b2-b9a89a84332f"
              },
              {
                "type": "row",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "md"
                    }
                  }
                },
                "children": [
                  {
                    "type": "@stat_card",
                    "properties": {
                      "label": {
                        "stringVal": {
                          "value": "Agentes Usados"
                        }
                      },
                      "value": {
                        "stringVal": {
                          "value": "24"
                        }
                      }
                    },
                    "editorId": "6638a620-5138-4b5f-9a7f-53fb7c075fcf"
                  },
                  {
                    "type": "@stat_card",
                    "properties": {
                      "label": {
                        "stringVal": {
                          "value": "Horas Salvas"
                        }
                      },
                      "value": {
                        "stringVal": {
                          "value": "128h"
                        }
                      }
                    },
                    "editorId": "c701370c-ad47-4932-9a54-d76eded2741e"
                  },
                  {
                    "type": "@stat_card",
                    "properties": {
                      "label": {
                        "stringVal": {
                          "value": "Créditos"
                        }
                      },
                      "value": {
                        "stringVal": {
                          "value": "Ilimitado"
                        }
                      }
                    },
                    "editorId": "51b967ad-97ce-4755-a8df-4f1ce0c8fe9e"
                  }
                ],
                "editorId": "a0161748-2456-4311-8296-48e39205be65"
              }
            ],
            "editorId": "8b9721d6-c003-43e0-b379-0fd281984b57"
          },
          {
            "type": "column",
            "properties": {
              "cross_align": {
                "align": {
                  "named": "stretch"
                }
              },
              "spacing": {
                "stringVal": {
                  "value": "md"
                }
              },
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "rightToken": "lg",
                  "leftToken": "lg"
                }
              }
            },
            "children": [
              {
                "type": "row",
                "properties": {
                  "align": {
                    "align": {
                      "named": "space_between"
                    }
                  },
                  "cross_align": {
                    "align": {
                      "named": "center"
                    }
                  }
                },
                "children": [
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Histórico Recente"
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "title_medium"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "primary_text"
                        }
                      },
                      "font_weight": {
                        "numberVal": {
                          "value": 700
                        }
                      }
                    },
                    "editorId": "c0dbaaa6-7081-41a7-90eb-8ef159dfee15"
                  },
                  {
                    "type": "text",
                    "properties": {
                      "content": {
                        "stringVal": {
                          "value": "Ver tudo"
                        }
                      },
                      "style": {
                        "textStyle": {
                          "styleName": "label_small"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "secondary_text"
                        }
                      }
                    },
                    "editorId": "eb5c4b78-1a9d-49d2-b2a0-b4d1222ad296"
                  }
                ],
                "editorId": "137410bd-953b-4ac2-9b19-7b337fcccfdc"
              },
              {
                "type": "column",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "sm"
                    }
                  }
                },
                "children": [
                  {
                    "type": "@history_item",
                    "properties": {
                      "name": {
                        "stringVal": {
                          "value": "Art Gen Pro"
                        }
                      },
                      "date": {
                        "stringVal": {
                          "value": "Hoje, 14:20"
                        }
                      },
                      "img": {
                        "stringVal": {
                          "value": "cyberpunk digital art"
                        }
                      }
                    },
                    "editorId": "02b8f8fb-4251-4c61-8231-8110fb6cbd37"
                  },
                  {
                    "type": "@history_item",
                    "properties": {
                      "name": {
                        "stringVal": {
                          "value": "Copy Master"
                        }
                      },
                      "date": {
                        "stringVal": {
                          "value": "Ontem, 09:15"
                        }
                      },
                      "img": {
                        "stringVal": {
                          "value": "typewriter neon"
                        }
                      }
                    },
                    "editorId": "0c5cbc5f-3b4a-438b-95cc-241c14d2853e"
                  },
                  {
                    "type": "@history_item",
                    "properties": {
                      "name": {
                        "stringVal": {
                          "value": "Bug Hunter"
                        }
                      },
                      "date": {
                        "stringVal": {
                          "value": "22 Out, 18:45"
                        }
                      },
                      "img": {
                        "stringVal": {
                          "value": "matrix code green"
                        }
                      }
                    },
                    "editorId": "6be1568e-18d1-4e93-8c38-ea74cdb99e5b"
                  },
                  {
                    "type": "@history_item",
                    "properties": {
                      "name": {
                        "stringVal": {
                          "value": "Video Edit AI"
                        }
                      },
                      "date": {
                        "stringVal": {
                          "value": "20 Out, 11:30"
                        }
                      },
                      "img": {
                        "stringVal": {
                          "value": "video production studio"
                        }
                      }
                    },
                    "editorId": "976c5cfa-d43a-4fca-acf5-8b5dbbca5887"
                  }
                ],
                "editorId": "c3bf15b1-d620-4178-9bc3-cf032108c204"
              }
            ],
            "editorId": "536a9479-f1bf-43a7-bd95-a5843a5a3043"
          },
          {
            "type": "container",
            "properties": {
              "margin": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "token": "lg"
                }
              },
              "padding": {
                "edgeInsets": {
                  "top": 0,
                  "right": 0,
                  "bottom": 0,
                  "left": 0,
                  "token": "lg"
                }
              },
              "radius": {
                "radius": {
                  "topLeft": 0,
                  "topRight": 0,
                  "bottomLeft": 0,
                  "bottomRight": 0,
                  "token": "lg"
                }
              },
              "gradient": {
                "gradient": {
                  "type": "GRADIENT_TYPE_LINEAR",
                  "direction": "45",
                  "stops": [
                    {
                      "color": "surface"
                    },
                    {
                      "color": "primary/20"
                    }
                  ]
                }
              },
              "border": {
                "border": {
                  "width": 1,
                  "color": "divider"
                }
              }
            },
            "children": [
              {
                "type": "row",
                "properties": {
                  "spacing": {
                    "stringVal": {
                      "value": "md"
                    }
                  }
                },
                "children": [
                  {
                    "type": "icon",
                    "properties": {
                      "name": {
                        "icon": {
                          "name": "card_giftcard_rounded"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "on_primary"
                        }
                      },
                      "size": {
                        "numberVal": {
                          "value": 32
                        }
                      }
                    },
                    "editorId": "87e0c9fc-d0b3-4f32-9a1a-d908edae7d18"
                  },
                  {
                    "type": "expanded",
                    "children": [
                      {
                        "type": "column",
                        "properties": {
                          "cross_align": {
                            "align": {
                              "named": "start"
                            }
                          },
                          "spacing": {
                            "numberVal": {
                              "value": 2
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Indique um amigo"
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "body_large"
                                }
                              },
                              "font_weight": {
                                "stringVal": {
                                  "value": "bold"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "primary_text"
                                }
                              }
                            },
                            "editorId": "6708451a-4f0c-46ed-9770-48787a8973c9"
                          },
                          {
                            "type": "text",
                            "properties": {
                              "content": {
                                "stringVal": {
                                  "value": "Ganhe 15 dias de acesso VIP para cada novo membro."
                                }
                              },
                              "style": {
                                "textStyle": {
                                  "styleName": "body_small"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "secondary_text"
                                }
                              }
                            },
                            "editorId": "8b5f2cf7-c54c-4cd7-91b5-935cacb95dde"
                          }
                        ],
                        "editorId": "b5991ff8-3ff4-4385-8994-a33cd169c9ad"
                      }
                    ],
                    "editorId": "489781ba-296c-47a1-8484-449625255c45"
                  },
                  {
                    "type": "icon",
                    "properties": {
                      "name": {
                        "icon": {
                          "name": "arrow_forward_ios_rounded"
                        }
                      },
                      "color": {
                        "color": {
                          "color": "secondary_text"
                        }
                      },
                      "size": {
                        "numberVal": {
                          "value": 16
                        }
                      }
                    },
                    "editorId": "0ac5174a-25ae-42c3-8381-429edec26734"
                  }
                ],
                "editorId": "0bff697a-b593-4d5d-92cc-42eae13c0c1d"
              }
            ],
            "editorId": "cb2435c4-1786-44ed-8a61-974858554b95"
          },
          {
            "type": "sizedbox",
            "properties": {
              "height": {
                "stringVal": {
                  "value": "xl"
                }
              }
            },
            "editorId": "5521d374-21b9-49f1-829a-58f45d6dbef8"
          },
          {
            "type": "stack",
            "properties": {
              "align_y": {
                "numberVal": {
                  "value": -1
                }
              }
            },
            "children": [
              {
                "type": "container",
                "properties": {
                  "height": {
                    "px": {
                      "value": 60,
                      "isInfinity": false
                    }
                  },
                  "width": {
                    "px": {
                      "value": "Infinity",
                      "isInfinity": true
                    }
                  },
                  "padding": {
                    "edgeInsets": {
                      "top": 0,
                      "right": 0,
                      "bottom": 0,
                      "left": 0,
                      "rightToken": "lg",
                      "leftToken": "lg"
                    }
                  }
                },
                "children": [
                  {
                    "type": "row",
                    "properties": {
                      "align": {
                        "align": {
                          "named": "space_between"
                        }
                      },
                      "cross_align": {
                        "align": {
                          "named": "center"
                        }
                      }
                    },
                    "children": [
                      {
                        "type": "iconbutton",
                        "properties": {
                          "name": {
                            "icon": {
                              "name": "arrow_back_rounded"
                            }
                          },
                          "color": {
                            "color": {
                              "color": "primary_text"
                            }
                          },
                          "bg": {
                            "color": {
                              "color": "surface",
                              "opacityPercent": 60
                            }
                          },
                          "radius": {
                            "radius": {
                              "topLeft": 0,
                              "topRight": 0,
                              "bottomLeft": 0,
                              "bottomRight": 0,
                              "token": "full"
                            }
                          }
                        },
                        "editorId": "ef70008c-87bc-40e0-b04f-bc5d97e59b1f"
                      },
                      {
                        "type": "row",
                        "properties": {
                          "spacing": {
                            "stringVal": {
                              "value": "sm"
                            }
                          }
                        },
                        "children": [
                          {
                            "type": "iconbutton",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "settings_rounded"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "primary_text"
                                }
                              },
                              "bg": {
                                "color": {
                                  "color": "surface",
                                  "opacityPercent": 60
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "full"
                                }
                              }
                            },
                            "editorId": "fbeb5202-b65d-4e56-8971-003b17475c89"
                          },
                          {
                            "type": "iconbutton",
                            "properties": {
                              "name": {
                                "icon": {
                                  "name": "logout_rounded"
                                }
                              },
                              "color": {
                                "color": {
                                  "color": "error"
                                }
                              },
                              "bg": {
                                "color": {
                                  "color": "surface",
                                  "opacityPercent": 60
                                }
                              },
                              "radius": {
                                "radius": {
                                  "topLeft": 0,
                                  "topRight": 0,
                                  "bottomLeft": 0,
                                  "bottomRight": 0,
                                  "token": "full"
                                }
                              }
                            },
                            "editorId": "f0ad51ef-fc94-43cf-8868-f1a1d3d5f72e"
                          }
                        ],
                        "editorId": "cb76a596-ca11-44c5-bb55-ce0838b5f2af"
                      }
                    ],
                    "editorId": "8eb1defa-7422-4934-8466-d52628fbfd40"
                  }
                ],
                "editorId": "22eb2064-a051-4c69-8288-9600c3a668c1"
              }
            ],
            "editorId": "d27894e8-3477-4153-9b3c-bcc1c6203ac6"
          }
        ],
        "editorId": "2299df2a-d23b-4212-a1dd-449a1e56c133"
      }
    ],
    "editorId": "9e1d2ee9-1fbf-4413-a723-15f115113ea2"
  }
}
```
