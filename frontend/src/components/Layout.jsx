import PropTypes from 'prop-types';

function Layout({ children }) {
  return (
    <div className="layout">
      <header className="layout__header">
        <h1>FastAPI + React Boilerplate</h1>
        <p>Stack listo para desarrollar aplicaciones modernas.</p>
      </header>
      <main className="layout__content">{children}</main>
      <footer className="layout__footer">
        <small>&copy; {new Date().getFullYear()} FastAPI + React Boilerplate</small>
      </footer>
    </div>
  );
}

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;
