import Layout from './components/Layout.jsx';
import HealthStatus from './components/HealthStatus.jsx';

function App() {
  return (
    <Layout>
      <section className="card">
        <h2>Estado del backend</h2>
        <HealthStatus />
      </section>
    </Layout>
  );
}

export default App;
