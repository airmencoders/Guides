const config = {
  gatsby: {
    pathPrefix: '/',
    siteUrl: 'https://oteguide.il2.dso.mil/',
    gaTrackingId: null,
    trailingSlash: false,
  },
  header: {
    logo: '', // src/components/images/logo.svg
    logoLink: 'https://oteguide.il2.dso.mil/',
    title: "<a href='https://oteguide.il2.dso.mil/'>AFOTEC OT&E Guide</a>",
    githubUrl: '',
    helpUrl: '',
    tweetText: '',
    /*
    social: `<li>
		    <a href="https://twitter.com/hasurahq" target="_blank" rel="noopener">
		      <div class="twitterBtn">
		        <img src='https://graphql-engine-cdn.hasura.io/learn-hasura/assets/homepage/twitter-brands-block.svg' alt={'Discord'}/>
		      </div>
		    </a>
		  </li>
			<li>
		    <a href="https://discordapp.com/invite/hasura" target="_blank" rel="noopener">
		      <div class="discordBtn">
		        <img src='https://graphql-engine-cdn.hasura.io/learn-hasura/assets/homepage/discord-brands-block.svg' alt={'Discord'}/>
		      </div>
		    </a>
      </li>`,
      */
    links: [{ text: '', link: '' }],
    search: {
      enabled: true,
      indexName: 'il2_guide',
      algoliaAppId: process.env.GATSBY_ALGOLIA_APP_ID,
      algoliaSearchKey: process.env.GATSBY_ALGOLIA_SEARCH_KEY,
      algoliaAdminKey: process.env.ALGOLIA_ADMIN_KEY,
    },
  },
  sidebar: {
    // add trailing slash if enabled above. Use this area to force an order. ex '/introduction',  '/codeblock',
    forcedNavOrder: [
      '/OT&E_Guide',
      '/fn_guides',
      '/OTE_construct_development_guide',
      '/accreditation_guide',
      '/analyst_test_design_guide',
      '/editing_reports_guide',
      '/evaluation_and_reporting_guide',
      '/lessons_learned_guide',
      '/measures_guide',
      '/safety_risk_mgmt_guide',
      '/strat_planning_programming_guide',
      '/test_capability_guide',
      '/acronyms',
      '/glossary',
    ],
    collapsedNav: [
      '/OT&E_Guide',
      '/OTE_construct_development_guide',
      '/OTE_construct_development_guide',
      '/accreditation_guide',
      '/analyst_test_design_guide',
      '/editing_reports_guide',
      '/evaluation_and_reporting_guide',
      '/lessons_learned_guide',
      '/measures_guide',
      '/safety_risk_mgmt_guide',
      '/strat_planning_programming_guide',
      '/test_capability_guide',
    ],
    links: [
      { text: 'AFOTEC', link: 'https://www.afotec.af.mil' },
      { text: 'Cyber Support Package Guide', link: 'https://usaf.dps.mil/:w:/r/sites/AFOTEC-PRIVATE/mainlibrary/oteguide/Shared%20Documents/Functional%20Guides/AFOTEC%20Cyber%20Support%20Package%20Guide.docx?d=wa256f83b0e4c475485e72f4a383f81a3&csf=1&web=1&e=C2RUBJ' },
      { text: 'Risk Assessment and Level of Test (RALOT) Guide', link: 'https://cs2.eis.af.mil/sites/10008/library/jobaidsguides/AFOTEC%20RALOT%20Guide%20Template.dotx?Web=1' },
      {
        text: 'OT&E Templates/Job Aids',
        link: 'https://usaf.dps.mil/sites/AFOTEC-PRIVATE/mainlibrary/',
      },
      {
        text: 'OT&E Tools Catalog',
        link:
          'https://usaf.dps.mil/sites/AFOTEC-PRIVATE/mainlibrary/oteguide/SitePages/Tools-Page.aspx',
      },
    ],
    frontline: true,
    ignoreIndex: true,
    title: '',
  },
  siteMetadata: {
    title: 'AFOTEC OT&E Guide',
    description: 'Air Force Operational Test and Evaluation Guide',
    ogImage: null,
    docsLocation: '',
    favicon: 'https://raw.githubusercontent.com/Travis42/misc/main/favicon.ico', //TODO: icons in place, but not working. Might need SVG
  },
  pwa: {
    enabled: false, // disabling this will also remove the existing service worker.
    manifest: {
      name: 'AFOTEC OT&E Guide',
      short_name: 'OT&E Guide',
      start_url: '/',
      background_color: '#6b37bf',
      theme_color: '#6b37bf',
      display: 'standalone',
      crossOrigin: 'use-credentials',
      icons: [
        {
          src: 'src/pwa-512.png',
          sizes: `512x512`,
          type: `image/png`,
        },
      ],
    },
  },
};

module.exports = config;
